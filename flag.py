import os
dot = (["."] * 65) + (["@"] * 15)
dots = {}

for i in range(10) :
    dots[f"dot{i}"] = dot.copy()
    dot = [dot[-1]] + dot[:-1]

laps = 5
counter = 80.33 * laps
while counter > 0 :
    os.system("clear")

    for i in range(10) :
        print("".join(dots[f"dot{i}"]))
        dots[f"dot{i}"] = [dots[f"dot{i}"][-1]] + dots[f"dot{i}"][:-1]
    counter -= 1
