from datetime import date, timedelta


class Equipment:
    def __init__(self, code, name):
        code = code.strip().upper()
        if not code:
            raise ValueError("ID cannot be blank.")
        self.__code = code
        self.rename(name)
        self.__student = ""
        self.__due = None

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_student(self):
        return self.__student

    def get_due(self):
        return self.__due

    def rename(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Name cannot be blank.")
        self.__name = name

    def loan_days(self):
        return 1
