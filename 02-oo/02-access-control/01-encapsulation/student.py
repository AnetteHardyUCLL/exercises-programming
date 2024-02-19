class Wizard:
    def __init__(self, name):
        self.name = name
        self.__mana = 45
        self.__health = 65

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health
