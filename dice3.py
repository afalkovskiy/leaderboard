# roll dice

import random

DICE_ART = {

    1: (

        "┌─────────┐",

        "│         │",

        "│    ●    │",

        "│         │",

        "└─────────┘",

    ),

    2: (

        "┌─────────┐",

        "│  ●      │",

        "│         │",

        "│      ●  │",

        "└─────────┘",

    ),

    3: (

        "┌─────────┐",

        "│  ●      │",

        "│    ●    │",

        "│      ●  │",

        "└─────────┘",

    ),

    4: (

        "┌─────────┐",

        "│  ●   ●  │",

        "│         │",

        "│  ●   ●  │",

        "└─────────┘",

    ),

    5: (

        "┌─────────┐",

        "│  ●   ●  │",

        "│    ●    │",

        "│  ●   ●  │",

        "└─────────┘",

    ),

    6: (

        "┌─────────┐",

        "│  ●   ●  │",

        "│  ●   ●  │",

        "│  ●   ●  │",

        "└─────────┘",

    ),

}

# A = DICE_ART[3]
# for Aj in A:
#     print(Aj)

print("\n*** Dice Guess Game ***")
print('Which number it lands?\n')

n_true = 0
n_all = 0

for i in range(10):
    try:
        g = int(input("Your guess [1-6]:"))
    except ValueError:
        print("That is not int!")
        continue    
    d = random.randrange(1,6)
    print("Rolled: ", d)
    A = DICE_ART[d]
    for Aj in A:
        print(Aj)
    n_all = n_all + 1
    if (g==d):
        n_true = n_true + 1
        print('Bingo!')

print("correct ", n_true, " out of ", n_all)
score = 100.*n_true/n_all

print("your score is ", round(score,2))