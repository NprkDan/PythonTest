# guessing game #

import random

target = random.randint(1, 11)
guess = 0

while guess != target:
    guess += 1
    print("guessing", guess)
    break
else:
    print("Correct", target)
    
