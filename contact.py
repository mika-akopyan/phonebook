from __future__ import annotations
import re


class Manager:
    """
    Предназначен для управления данными телефонного справочника.
    """
    def filter(self, **kwargs: dict[str, str]) -> list[Contact] | None:
        """
        Возвращает список, содержащий объекты типа Contact,
        которые соответствуют заданным параметрам поиска, либо None, если не найден ни один объект.
        """
        search_criteria = kwargs
        list_objects = []

        with open("phonebook.txt", "r", encoding="utf-8") as file:
            for line in file:
                data = line[:(len(line)-1)].split('; ')
                contact = Contact(data[0], data[1], data[2], data[3], data[4], data[5])
                contact._old_version = line
                if self.__is_satisfies_search(search_criteria, contact):
                    list_objects.append(contact)

        if len(list_objects) == 0:
            return None
        else:
            return list_objects

    def __is_satisfies_search(self, search_criteria: dict, contact: Contact) -> bool:
        """
        Возвращает True, если все критерии поиска для объекта удовлетворены, иначе False.
        """
        for criteria in search_criteria:
            if getattr(contact, criteria) is not None:
                if not (getattr(contact, criteria) == search_criteria[criteria]):
                    return False
            else:
                raise AttributeError(f'"Contact" не содержит атрибут {criteria}')
                return False
            
        return True
    
    def get(self, **kwargs: dict[str, str]) -> Contact | None:
        """
        Возвращает один объект типа Contact, который соответствует заданным параметрам поиска.
        """
        list_objects = self.filter(**kwargs)

        if list_objects is None:
            return None
        elif len(list_objects) > 1:
            raise Exception('По указанным критериям было найдено более одного объекта.')
        else:
            return list_objects[0]
        
    def print_all(self) -> None:
        """
        Построчно выводит на экран все записи из телефонного справочника.
        """
        with open("phonebook.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line, end='')

    def create(self, surname: str, name: str, patronymic: str, organization: str, work_number: str, personal_number: str):
        """
        Создает и сохраняет объект.
        """
        Contact(surname, name, patronymic, organization, work_number, personal_number).save()


class Contact:
    """
    Представляет контакт из телефонного справочника.
    """
    objects = Manager()

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
        error_msg = ("Фамилия должна быть строковым значением, "
                     "может содержать прописные и строчные буквы русского алфавита, "
                     "дефис и апостроф.")
        
        # Проверка валидности данных
        if not isinstance(surname, str):
            raise TypeError(error_msg)
        elif re.fullmatch("[А-Яа-я'-]+", surname) is None:
            raise ValueError(error_msg)
        else:
            self.__surname = surname

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        error_msg = ("Имя должно быть строковым значением, "
                     "может содержать прописные и строчные буквы русского алфавита, "
                     "дефис и апостроф.")
        
        # Проверка валидности данных
        if not isinstance(name, str):
            raise TypeError(error_msg)
        elif re.fullmatch("[А-Яа-я'-]+", name) is None:
            raise ValueError(error_msg)
        else:
            self.__name = name

    @property
    def patronymic(self) -> str:
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic: str):
        error_msg = ("Отчество должно быть строковым значением, "
                     "может содержать прописные и строчные буквы русского алфавита, "
                     "дефис и апостроф.")
                    
        # Проверка валидности данных
        if not isinstance(patronymic, str):
            raise TypeError(error_msg)
        elif re.fullmatch("[А-Яа-я'-]+", patronymic) is None:
            raise ValueError(error_msg)
        else:
            self.__patronymic = patronymic

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        error_msg = "Название организации должно быть строковым значением, не может содержать символ ';'."

        # Проверка валидности данных
        if not isinstance(organization, str):
            raise TypeError(error_msg)
        elif re.search(';', organization) is not None:
            raise ValueError(error_msg)
        else:
            self.__organization = organization.strip()

    @property
    def work_number(self) -> str:
        return self.__work_number

    @work_number.setter
    def work_number(self, work_number: str):
        error_msg = ("Рабочий номер телефона должен быть строковым значением в формате 8-XXX-XXX-XX-XX, "
                     "где X - любое целое число от 0 до 9.")
        
        # Проверка валидности данных
        if not isinstance(work_number, str):
            raise TypeError(error_msg)
        elif re.fullmatch("8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}", work_number) is None:
            raise ValueError(error_msg)
        else:
            self.__work_number = work_number

    def __is_unique_number(self, number: str) -> bool:
        """
        Возвращает True, если номер является уникальным, иначе False.
        """
        if self.work_number == self.personal_number:
            raise ValueError("Рабочий и личный телефоны не должны совпадать!")
            return False
        elif self.__has_number_in_file(number):
            return False
        
        return True
        
    def __has_number_in_file(self, number: str) -> bool:
        """
        Возвращает True, если данный номер уже существует в справочнике, иначе False.
        """
        with open("phonebook.txt", "r", encoding="utf-8") as file:
            if self._old_version is None:
                for line in file:
                    if line.find(number) != -1:
                        if number == self.work_number:
                            raise ValueError("Контакт с данным рабочим номером уже существует в справочнике!")
                            return True
                        elif number == self.personal_number:
                            raise ValueError("Контакт с данным личным номером уже существует в справочнике!")
                            return True
            else:
                data = file.read().replace(self._old_version, '')
                if data.find(number) != -1:
                    if number == self.work_number:
                                raise ValueError("Контакт с данным рабочим номером уже существует в справочнике!")
                                return True
                    elif number == self.personal_number:
                        raise ValueError("Контакт с данным личным номером уже существует в справочнике!")
                        return True
        
        return False

    @property
    def personal_number(self) -> str:
        return self.__personal_number

    @personal_number.setter
    def personal_number(self, personal_number: str):
        error_msg = ("Личный номер телефона должен быть строковым значением в формате 8-XXX-XXX-XX-XX, "
                     "где X - любое целое число от 0 до 9.")
        
        # Проверка валидности данных
        if not isinstance(personal_number, str):
            raise TypeError(error_msg)
        elif re.fullmatch("8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}", personal_number) is None:
            raise ValueError(error_msg)
        else:
            self.__personal_number = personal_number

    def save(self):
        """
        Сохраняет контакт в телефонном справочнике.
        """
        if self.surname is None:
            raise AttributeError('Укажите фамилию.')
        elif self.name is None:
            raise AttributeError('Укажите имя.')
        elif self.patronymic is None:
            raise AttributeError('Укажите отчество.')
        elif self.organization is None:
            raise AttributeError('Укажите название организации.')
        elif self.work_number is None:
            raise AttributeError('Укажите рабочий номер телефона.')
        elif self.personal_number is None:
            raise AttributeError('Укажите личный номер телефона.')
        elif self.__is_unique_number(self.work_number) and self.__is_unique_number(self.personal_number):
            if self._old_version is None:
                self.__insert()
            else:
                self.__update()

    def __insert(self):
        """
        Вставляет запись в справочник.
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

    def __update(self):
        """
        Обновляет запись в справочнике.
        """
        with open("phonebook.txt", "r", encoding="utf-8") as file:
            new_version = '; '.join([str(self.surname),
                                     str(self.name),
                                     str(self.patronymic),
                                     str(self.organization),
                                     str(self.work_number),str(self.personal_number)]) + '\n'
            data = file.read()
            data = data.replace(self._old_version, new_version)
        
        with open("phonebook.txt", "w", encoding="utf-8") as file:
            file.write(data)

    def show_info(self) -> None:
        """
        Отображает информацию о текущем контакте.
        """
        print(
            '; '.join([str(self.surname),
                       str(self.name),
                       str(self.patronymic),
                       str(self.organization),
                       str(self.work_number),str(self.personal_number)])
        )

    def __getattr__(self, name) -> None:
        return None
