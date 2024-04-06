# roll dice

import random

n_true = 0
n_all = 0

for i in range(20):
    g = int(input("your guess [1-6]:"))
    d = random.randrange(1,6)
    print("Rolled: ", d)
    n_all = n_all + 1
    if (g==d):
        n_true = n_true + 1
        print('Bingo!')

print("correct ", n_true, " out of ", n_all)
score = 100.*n_true/n_all

print("your score is ", score)