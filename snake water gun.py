'''snake vs water -snake wins
water vs gun - water wins
gun vs snake gun wins'''

import random


a=random.choice(["water","snake","gun"])
b=input("user b turn- ")
print(f"computer choose {[a]}")


if ((a== "snake" and b == "water") or (a=="water" and b=="gun") or (a=="gun"and b=="snake") ):
    print("computer wins")
elif ((b== "snake" and a == "water") or (b=="water" and a=="gun") or (b=="gun"and a=="snake")):
    print("user b wins")
elif((b==a)):
    print("draw")
else:
    print("invalid input")
