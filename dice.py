# roll dice

import random

for i in range(10):
    g = input("your guess [1-6]:")
    d = random.randrange(1,6)
    print("Rolled: ", d)