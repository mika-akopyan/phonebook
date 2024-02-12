import re

class Contact:
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname:str):
        # Проверка корректности типов данных
        if isinstance(surname, str):
            self.__surname = surname
        else:
            raise TypeError('Ожидается строковое значение!')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name:str):
        # Проверка корректности типов данных
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError('Ожидается строковое значение!')

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic:str):
        # Проверка корректности типов данных
        if isinstance(patronymic, str):
            self.__patronymic = patronymic
        else:
            raise TypeError('Ожидается строковое значение!')
    
    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, organization:str):
        # Проверка корректности типов данных
        if isinstance(organization, str):
            self.__organization = organization
        else:
            raise TypeError('Ожидается строковое значение!')

    @property
    def work_number(self):
        return self.__work_number

    @work_number.setter
    def work_number(self, work_number:str):
        # Проверка корректности типов данных
        if re.fullmatch('8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}', work_number) is None:
            raise TypeError('Ожидается значение в формате 8-XXX-XXX-XX-XX, где X - любое число от 0 до 9!')
        else:
            self.__work_number = work_number

    @property
    def personal_number(self):
        return self.__personal_number

    @personal_number.setter
    def personal_number(self, personal_number:str):
        # Проверка корректности типов данных
        if re.fullmatch('8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}', personal_number) is None:
            raise TypeError('Ожидается значение в формате 8-XXX-XXX-XX-XX, где X - любое число от 0 до 9!')
        else:
            self.__personal_number = personal_number
