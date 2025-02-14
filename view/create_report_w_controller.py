from PyQt6.QtWidgets import QFileDialog, QMessageBox
import pandas as pd
import os
from openpyxl.styles import Alignment
from service.bank_services_manager import BankServicesManager


def create_report(self):
    client_query = self.client_line_edit.text().strip()
    service_filter = self.filter_combo_box.currentText()

    start_date_str = self.start_date_edit.date().toString("dd.MM.yyyy")
    end_date_str = self.end_date_edit.date().toString("dd.MM.yyyy")
    start_date_obj = self.start_date_edit.date().toPyDate()
    end_date_obj = self.end_date_edit.date().toPyDate()

    if client_query:
        filtered_clients = [
            client for client in self.clients
            if client_query.lower() in client.full_name.lower()
        ]
    else:
        filtered_clients = self.clients

    if not filtered_clients:
        QMessageBox.warning(
            self,
            "Предупреждение",
            "Клиенты не найдены по заданному запросу."
        )
        return

    services_manager = BankServicesManager()
    report_data = []

    for client in filtered_clients:
        accounts_all = services_manager.get_accounts_for_client(client.id) or [
        ]
        accounts = [acc for acc in accounts_all if start_date_obj <=
                    acc.opened_date <= end_date_obj]
        if accounts:
            acc_details = []
            for account in accounts:
                detail = (
                    f"Тип: {account.type}, Номер: {account.number}, Валюта: {account.currency}, "
                    f"Баланс: {account.balance}, Дата открытия: {account.opened_date.strftime('%d.%m.%Y')}\n"
                )
                if account.closed_date:
                    detail += f", Дата закрытия: {account.closed_date.strftime('%d.%m.%Y')}"
                acc_details.append(detail)
            accounts_info = "\n".join(acc_details)
        else:
            accounts_info = "Нет данных"

        cards_all = services_manager.get_cards_for_client(client.id) or []
        cards = [card for card in cards_all if start_date_obj <=
                 card.opened_date <= end_date_obj]
        if cards:
            card_details = []
            for card in cards:
                detail = (
                    f"Тип: {card.type}, Номер карты: {card.number}, "
                    f"Счет: {card.account.number}, Срок действия: {card.expiration_date.strftime('%d.%m.%Y')}\n"
                )
                if card.credit_limit != 0.00:
                    detail += f", Кредитный лимит: {card.credit_limit} {card.account.currency}"
                detail += f", Дата открытия: {card.opened_date.strftime('%d.%m.%Y')}"
                if card.closed_date:
                    detail += f", Дата закрытия: {card.closed_date.strftime('%d.%m.%Y')}"
                card_details.append(detail)
            cards_info = "\n".join(card_details)
        else:
            cards_info = "Нет данных"

        deposits_all = services_manager.get_deposits_for_client(client.id) or [
        ]
        deposits = [deposit for deposit in deposits_all if start_date_obj <=
                    deposit.opened_date <= end_date_obj]
        if deposits:
            deposit_details = []
            for deposit in deposits:
                detail = (
                    f"Тип: {deposit.type}, Сумма: {deposit.amount}, Процент: {deposit.interest_rate}%, "
                    f"Дата погашения: {deposit.due_date.strftime('%d.%m.%Y')}, Дата открытия: {deposit.opened_date.strftime('%d.%m.%Y')}\n"
                )
                if deposit.closed_date:
                    detail += f", Дата закрытия: {deposit.closed_date.strftime('%d.%m.%Y')}"
                deposit_details.append(detail)
            deposits_info = "\n".join(deposit_details)
        else:
            deposits_info = "Нет данных"

        credits_all = services_manager.get_credits_for_client(client.id) or []
        credits = [credit for credit in credits_all if start_date_obj <=
                   credit.opened_date <= end_date_obj]
        if credits:
            credit_details = []
            for credit in credits:
                detail = (
                    f"Тип: {credit.type}, Сумма: {credit.amount} RUB, Процент: {credit.interest_rate}%, "
                    f"Дата погашения: {credit.due_date.strftime('%d.%m.%Y')}, Месячный платеж: {credit.monthly_payment}\n"
                )
                if credit.closed_date:
                    detail += f", Дата закрытия: {credit.closed_date.strftime('%d.%м.%Y')}"
                credit_details.append(detail)
            credits_info = "\n".join(credit_details)
        else:
            credits_info = "Нет данных"

        if service_filter != "Выбрать все":
            if service_filter == "Счета":
                cards_info = deposits_info = credits_info = "Нет данных"
            elif service_filter == "Карты":
                accounts_info = deposits_info = credits_info = "Нет данных"
            elif service_filter == "Депозиты":
                accounts_info = cards_info = credits_info = "Нет данных"
            elif service_filter == "Кредиты":
                accounts_info = cards_info = deposits_info = "Нет данных"

        report_data.append({
            "ФИО": client.full_name,
            "Дата рождения": client.birth_date.strftime("%d.%m.%Y"),
            "Телефон": client.phone_number,
            "E-mail": client.email,
            "Период предоставления услуги": f"{start_date_str} - {end_date_str}",
            "Счета": accounts_info,
            "Карты": cards_info,
            "Депозиты": deposits_info,
            "Кредиты": credits_info
        })

    df = pd.DataFrame(report_data)

    file_path, _ = QFileDialog.getSaveFileName(
        self,
        "Сохранить отчет",
        "",
        "Excel Files (*.xlsx);;All Files (*)"
    )

    if file_path:
        try:
            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
                worksheet = writer.sheets["Sheet1"]
                for col in worksheet.columns:
                    max_length = 0
                    column = col[0].column_letter
                    for cell in col:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    if col[0].value in ["Счета", "Карты", "Депозиты", "Кредиты"]:
                        adjusted_width = max_length * 0.4
                    else:
                        adjusted_width = max_length
                    worksheet.column_dimensions[column].width = adjusted_width
                    for cell in col:
                        cell.alignment = Alignment(wrap_text=True)
            QMessageBox.information(
                self,
                "Успех",
                "Отчет успешно экспортирован в Excel."
            )
            os.system(f"open {file_path}")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Ошибка",
                f"Ошибка экспорта отчета:\n{e}"
            )
