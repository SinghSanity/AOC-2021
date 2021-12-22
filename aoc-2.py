f = open("inputD2.txt", "r")


horizontal_1 = 0
depth_1 = 0

horizontal_2 = 0
depth_2 = 0
aim = 0

for i in f:
    z = i.split()
    
    if z[0] == "forward":
        horizontal_1 += int(z[1])
        horizontal_2 += int(z[1])
        x = int(z[1]) * aim
        depth_2 += x


    elif z[0] == "up":
        depth_1 -= int(z[1])
        aim -= int(z[1])

    elif z[0] == "down":
        depth_1 += int(z[1])
        aim += int(z[1])
    else:
        continue
    print(aim)

f.close()
print("Part 1 answer: ")
print(depth_1 * horizontal_1)

print("Part 2 answer: ")
print(depth_2 * horizontal_2)