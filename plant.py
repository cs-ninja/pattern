from os import system
from time import sleep
import random

pot = """|_________________|
         |.................|
         |*****************|
         |=================|
         |@@@@@@@@@@@@@@@@@|
         |#################|
"""

go_down = 30
SideMaterial = ("🍀" , "🍃" , "" , "")
for i in range(go_down) :
    system("clear")
    print("\n" * go_down)


    width = "||" + ("|" * (i // 5))

    for j in range(i) :

        Lleaf = random.choice(SideMaterial)
        indentBY = (" " * 25)[:(-1 - (i // 10) - len(Lleaf))]
        Rleaf = random.choice(SideMaterial)

        stem = (f"{indentBY}{Lleaf}{width}{Rleaf}\n")
        stem = stem[:-1] 
        print(stem)

    print("\t\t" , "\n\t\t".join(pot.split()) , sep="")
    go_down -= 1
    sleep(0.2)
