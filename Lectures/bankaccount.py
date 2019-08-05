class BankAccount:

    def __init__(self, balance, name, age, phone, email):
        self.__balance = balance
        self.__name = name
        self.__age = age
        self.__phone = phone
        self.__email = email
    
    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email
    
    def set_balance(self, balance):
        self.__balance = balance

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return self.__name + ': ' + str(self.__balance)






    
