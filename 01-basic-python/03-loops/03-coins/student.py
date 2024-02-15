# Write your code here


def coins(one, two, five, goal):
    for i in range(0, one + 1):
        for j in range(0, two + 1):
            for k in range(0, five + 1):
                if i + 2 * j + 5 * k == goal:
                    return True
    return False
