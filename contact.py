import re


class Contact:
    def __init__(
        self,
        surname: str = None,
        name: str = None,
        patronymic: str = None,
        organization: str = None,
        work_number: str = None,
        personal_number: str = None,
    ) -> None:
        # Установка значений свойствам, если они были переданы в функцию
        if surname is not None:
            self.surname = surname

        if name is not None:
            self.name = name

        if patronymic is not None:
            self.patronymic = patronymic

        if organization is not None:
            self.organization = organization

        if work_number is not None:
            self.work_number = work_number

        if personal_number is not None:
            self.personal_number = personal_number

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        # Проверка валидности данных
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть строковым значением, может содержать прописные и строчные буквы русского алфавита, дефис и апостроф.")
        elif re.fullmatch("[А-Яа-я'-]+", surname) is None:
            raise ValueError("Фамилия должна быть строковым значением, может содержать прописные и строчные буквы русского алфавита, дефис и апостроф.")
        else:
            self.__surname = surname

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        # Проверка валидности данных
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строковым значением, может содержать прописные и строчные буквы русского алфавита, дефис и апостроф.")
        elif re.fullmatch("[А-Яа-я'-]+", name) is None:
            raise ValueError("Имя должно быть строковым значением, может содержать прописные и строчные буквы русского алфавита, дефис и апостроф.")
        else:
            self.__name = name

    @property
    def patronymic(self) -> str:
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic: str):
        # Проверка валидности данных
        if not isinstance(patronymic, str):
            raise TypeError("Отчество должно быть строковым значением, может содержать прописные и строчные буквы русского алфавита, дефис и апостроф.")
        elif re.fullmatch("[А-Яа-я'-]+", patronymic) is None:
            raise ValueError("Отчество должно быть строковым значением, может содержать прописные и строчные буквы русского алфавита, дефис и апостроф.")
        else:
            self.__patronymic = patronymic

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        # Проверка валидности данных
        if not isinstance(organization, str):
            raise TypeError("Наименование организации должно быть строковым значением, не может содержать символ ';'.")
        elif re.search(';', organization) is not None:
            raise ValueError("Наименование организации должно быть строковым значением, не может содержать символ ';'.")
        else:
            self.__organization = organization.strip()

    @property
    def work_number(self) -> str:
        return self.__work_number

    @work_number.setter
    def work_number(self, work_number: str):
        # Проверка валидности данных
        if not isinstance(work_number, str):
            raise TypeError(
                "Рабочий номер телефона должен быть строковым значением в формате 8-XXX-XXX-XX-XX, где X - любое число от 0 до 9!"
            )
        elif re.fullmatch("8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}", work_number) is None:
            raise ValueError(
                "Рабочий номер телефона должен быть строковым значением в формате 8-XXX-XXX-XX-XX, где X - любое число от 0 до 9!"
            )
        elif self.__is_unique_work_number(work_number):
                self.__work_number = work_number

    def __is_unique_work_number(self, work_number: str):
        """
        Возвращает true, если рабочий номер является уникальным, иначе false.
        """
        try:
            if self.personal_number == work_number:
                raise ValueError("Рабочий и личный телефоны не должны совпадать!")
                return False
        except AttributeError:
            pass
            
        if self.__has_number_in_file(work_number):
            raise ValueError("Контакт с данным номером уже существует в справочнике!")
            return False
        
        return True
        
    def __has_number_in_file(self, number: str) -> bool:
        """
        Возвращает true, если данный номер уже существует в справочнике, иначе false.
        """
        with open("phonebook.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.find(number) != -1:
                    return True
            
            return False

    @property
    def personal_number(self) -> str:
        return self.__personal_number

    @personal_number.setter
    def personal_number(self, personal_number: str):
        # Проверка валидности данных
        if not isinstance(personal_number, str):
            raise TypeError(
                "Личный номер телефона должен быть строковым значением в формате 8-XXX-XXX-XX-XX, где X - любое число от 0 до 9!"
            )
        elif re.fullmatch("8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}", personal_number) is None:
            raise ValueError(
                "Личный номер телефона должен быть строковым значением в формате 8-XXX-XXX-XX-XX, где X - любое число от 0 до 9!"
            )
        elif self.__is_unique_personal_number(personal_number):
                self.__personal_number = personal_number

    def __is_unique_personal_number(self, personal_number: str):
        """
        Возвращает true, если личный номер является уникальным, иначе false.
        """
        try:
            if self.work_number == personal_number:
                raise ValueError("Рабочий и личный телефоны не должны совпадать!")
                return False
        except AttributeError:
            pass
        
        if self.__has_number_in_file(personal_number):
            raise ValueError("Контакт с данным номером уже существует в справочнике!")
            return False
            
        return True

    def save(self):
        """
        Сохраняет контакт в телефонном справочнике.
        """
        with open("phonebook.txt", "a", encoding="utf-8") as file:
            file.write(
                self.surname + "; " +
                self.name + "; " +
                self.patronymic + "; " +
                self.organization + "; " +
                self.work_number + "; " +
                self.personal_number + "\n"
            )


class Manager:
    pass