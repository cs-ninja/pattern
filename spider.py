from os import system
from time import sleep



box = ("#"*20 , ) * 12

for _ in range(100) :
    sleep(0.12)
    system("clear")
    for num, index in enumerate(box) :
        if num % 2 == 0 :
            print("\t" , index, sep = "")
        else :
            print(index)
    sleep(0.12)
    system("clear")
    for num, index in enumerate(box) :
        if num % 2 != 0 :
            print("\t" , index, sep = "")
        else :
            print(index)

