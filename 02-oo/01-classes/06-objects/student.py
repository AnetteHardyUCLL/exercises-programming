def main():
    # write your code here
    brawler_aragorn = Brawler(4, 4, "Aragorn")
    brawler_gimli = Brawler(2, 7, "Gimli")
    brawler_legolas = Brawler(7, 7, "Legolas")
    brawler_frodo = Brawler(3, 2, "Frodo")

    fight(brawler_aragorn, brawler_gimli)
    fight(brawler_legolas, brawler_frodo)


# don't touch below this line


class Brawler:
    def __init__(self, speed, strength, name):
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        self.name = name


def fight(f1, f2):
    if f1.power > f2.power:
        print(f"{f1.name} wins with {f1.power} power over {f2.name}'s {f2.power}")
    elif f1.power < f2.power:
        print(f"{f2.name} wins with {f2.power} power over {f1.name}'s {f1.power}")
    else:
        print(f"It's a tie with both contestants at {f1.power} power")


main()
