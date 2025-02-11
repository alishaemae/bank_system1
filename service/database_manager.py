import configparser
import os
from sqlalchemy import create_engine, text
from data.query_result import QueryResult 
from data.user import UserRole


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.txt'))
db_url = config['database']['database_url']


class DatabaseManager:
    __engine = create_engine(db_url)

    def get_user_db(self, login):
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT id, role, job, last_name, first_name, middle_name, birth_date, address, phone_number, email, salary, login, password
                    FROM employees
                    WHERE login = :login and deleted is null""")
                result = conn.execute(query, {"login": login}).fetchone()
                return QueryResult(result, None)
        except Exception as e:
            return QueryResult(None, e)
    
    def get_clients_db(self, id_employee, role):
        try:
            with self.__engine.connect() as conn:
                if role == UserRole.BOSS:
                    query = text("""
                        SELECT c.id, c.id_employee, e.role, e.job, e.last_name, e.first_name, e.middle_name,
                                 c.last_name, c.first_name, c.middle_name, c.birth_date, c.phone_number, c.registration_address, c.residential_address, c.email, c.passport_number, c.passport_issue_date, c.inn, c.registration_date
                        FROM clients c
                        Join employees e on c.id_employee = e.id
                        """)
                else:
                    query = text("""
                        SELECT c.id, c.id_employee, e.role, e.job, e.last_name, e.first_name, e.middle_name,
                                 c.last_name, c.first_name, c.middle_name, c.birth_date, c.phone_number, c.registration_address, c.residential_address, c.email, c.passport_number, c.passport_issue_date, c.inn, c.registration_date
                        FROM clients c
                        Join employees e on c.id_employee = e.id
                        WHERE c.id_employee = :id_employee
                        """)
                result = conn.execute(query, {"id_employee": id_employee}).fetchall()
                return QueryResult(result, None)
        except Exception as e:
            return QueryResult(None, e)

    def get_client_info_db(self, id_client):
        try:
            with self.__engine.connect() as conn:
                query = text("""
                    SELECT c.id, c.id_employee, e.role, e.job, e.last_name, e.first_name, e.middle_name,
                             c.last_name, c.first_name, c.middle_name, c.birth_date, c.phone_number, c.registration_address, c.residential_address, c.email, c.passport_number, c.passport_issue_date, c.inn, c.registration_date
                    FROM clients c
                    Join employees e on c.id_employee = e.id
                    WHERE c.id = :id_client
                    """)
                result = conn.execute(query, {"id_client": id_client}).fetchone()
                return QueryResult(result, None)
        except Exception as e:
            return QueryResult(None, e)
                        
                        