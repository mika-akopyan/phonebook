class Contact:
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname:str):
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic:str):
        self.__patronymic = patronymic
    
    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, organization:str):
        self.__organization = organization

    @property
    def work_number(self):
        return self.__work_number

    @work_number.setter
    def work_number(self, work_number:str):
        self.__work_number = work_number

    @property
    def personal_number(self):
        return self.__personal_number

    @personal_number.setter
    def personal_number(self, personal_number:str):
        self.__personal_number = personal_number
