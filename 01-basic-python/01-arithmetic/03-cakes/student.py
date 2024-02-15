# Write your code here


def cakes(eggs, butter, flour):
    cakes_eggs = eggs // 5
    cakes_butter = butter // 250
    cakes_flour = flour // 250
    total_cakes = min(cakes_eggs, cakes_butter, cakes_flour)

    return total_cakes
