# Write your code here


def target_sum(ns, target):
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            if ns[i] + ns[j] == target:
                return True
    return False
