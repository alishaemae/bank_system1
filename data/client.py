class Client:
    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    
    @property
    def full_passport_info(self):
        return f"{self.passport_number} {self.passport_issue_date}"
     
    def __init__(self, id, employee,last_name, first_name, middle_name, birth_date, phone_number, registration_address, residential_address, email, passport_number, passport_issue_date, inn):
        self.id = int(id)
        self.employee = employee
        self.last_name = str(last_name)
        self.first_name = str(first_name)
        self.middle_name = str(middle_name)
        self.birth_date = birth_date
        self.phone_number = str(phone_number)
        self.registration_address = str(registration_address)
        self.residential_address = str(residential_address)
        self.email = str(email)
        self.passport_number = int(passport_number)
        self.passport_issue_date = passport_issue_date
        self.inn = int(inn)