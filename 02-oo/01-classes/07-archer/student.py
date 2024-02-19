class Archer:
    def __init__(self, name, health, num_arrows):
        pass

    def get_shot(self):
        pass

    def shoot(self, target):
        pass

    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")
