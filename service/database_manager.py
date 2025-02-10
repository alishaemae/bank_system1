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
