class Account:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    def is_correct_password(self, pw):
        return self.__password == pw
