f = open("inputD1.txt", "r")

count = 0
current = 0

first = 0
second = 0
third = 0

time = 1

for i in f:
    x = int(i)
    total = 0
    
    if first == 0:
        first = x
        continue
    if second == 0:
        second = x
        continue
    if third == 0:
        third = x

        total = first + second + third
        if total > current:
            current = total
            continue
    
    first = second
    second = third
    third = x
    temp = first + second + third
    if temp > current:
        count+=1
    current = temp
    

f.close()
print("Final count = " + str(count))
