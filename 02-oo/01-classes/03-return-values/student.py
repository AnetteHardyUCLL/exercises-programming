class Wall:
    armor = 10
    height = 5

    # write your code here
    def get_cost(self):
        return self.armor * self.height

    # don't touch below this line

    def fortify(self):
        self.armor *= 2
