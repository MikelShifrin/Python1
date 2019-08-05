class BankAccount:

    __balance = 0
    __name = ''
    __age = 0

    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_balance(self, balance):
        self.__balance = balance

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
