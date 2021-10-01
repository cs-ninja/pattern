from os import system
from time import sleep

rows = 20
mid = rows // 2
box = ["#"*20] * rows

for i in range(rows) :
    if i < mid :
        box[i] = (" " * i) + box[i]
    else :
        box[i] = (" " * (rows - i)) + box[i]

num1 = 30
num2 = 0
go_down = 0
for i in range(1000) :
    

    sleep(0.02)
    system("clear")
    if i <= num1 :
        go_down += 1
        print("\n" * go_down)
        if i == num1 :
            num2 += 60
    
    else :
        go_down -= 1
        print("\n" * go_down)
        if i == num2 :
            num1 += 60
    
    
    print("\n".join(box))
    box = box[1:] + [box[0]]

