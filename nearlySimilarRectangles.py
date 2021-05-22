# ===========================Nearest Similar Rectangle===========================
from math import factorial
from collections import Counter


def nearlySimilarRectangles(sides):
    # Write your code here
    count = 0
    lst = Counter([i[0] / i[1] for i in sides])
    for i in lst.keys():
        temp = lst[i]
        if temp > 2:
            flo = factorial(temp) / (factorial(2) * (factorial(temp - 2)))
            count += int(flo)
        elif temp == 2:
            count += 1
    return count
