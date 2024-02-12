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
        # Проверка корректности типов данных
        if isinstance(surname, str):
            self.__surname = surname.strip()
        else:
            raise TypeError("Ожидается строковое значение!")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        # Проверка корректности типов данных
        if isinstance(name, str):
            self.__name = name.strip()
        else:
            raise TypeError("Ожидается строковое значение!")

    @property
    def patronymic(self) -> str:
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic: str):
        # Проверка корректности типов данных
        if isinstance(patronymic, str):
            self.__patronymic = patronymic.strip()
        else:
            raise TypeError("Ожидается строковое значение!")

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        # Проверка корректности типов данных
        if isinstance(organization, str):
            self.__organization = organization.strip()
        else:
            raise TypeError("Ожидается строковое значение!")

    @property
    def work_number(self) -> str:
        return self.__work_number

    @work_number.setter
    def work_number(self, work_number: str):
        # Проверка корректности типов данных
        if re.fullmatch("8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}", work_number) is None:
            raise TypeError(
                "Ожидается значение в формате 8-XXX-XXX-XX-XX, где X - любое число от 0 до 9!"
            )
        else:
            if self.__is_unique_work_number(work_number):
                self.__work_number = work_number

    def __is_unique_work_number(self, work_number: str):
        """
        Возвращает true, если рабочий номер является уникальным, иначе false.
        """
        try:
            if self.personal_number == work_number:
                raise ValueError("Рабочий и личный телефоны не должны совпадать!")
                return False
            else:
                return True
        except AttributeError:
            return True

    @property
    def personal_number(self) -> str:
        return self.__personal_number

    @personal_number.setter
    def personal_number(self, personal_number: str):
        # Проверка корректности типов данных
        if (
            re.fullmatch("8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}", personal_number)
            is None
        ):
            raise TypeError(
                "Ожидается значение в формате 8-XXX-XXX-XX-XX, где X - любое число от 0 до 9!"
            )
        else:
            if self.__is_unique_personal_number(personal_number):
                self.__personal_number = personal_number

    def __is_unique_personal_number(self, personal_number: str):
        """
        Возвращает true, если личный номер является уникальным, иначе false.
        """
        try:
            if self.work_number == personal_number:
                raise ValueError("Рабочий и личный телефоны не должны совпадать!")
                return False
            else:
                return True
        except AttributeError:
            return True

    def save(self):
        """
        Сохраняет контакт в телефонном справочнике.
        """
        with open("phonebook.txt", "a", encoding="utf-8") as file:
            file.write(
                self.surname + ", " +
                self.name + ", " +
                self.patronymic + ", " +
                self.organization + ", " +
                self.work_number + ", " +
                self.personal_number + "\n"
            )
