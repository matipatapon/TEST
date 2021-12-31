import random as rand
table = []
d = 1000
for x in range(0,d + 1):
    for y in range(0,d + 1):
        z = x / d
        y = y / d
        table.append([z,y])
circle = 0
square = 0
for cord in table:
    distance = (cord[0] * cord[0] + cord[1] * cord[1])**0.5
    square +=1
    if distance <= 1:
        circle+=1
print((circle/square)*4)
