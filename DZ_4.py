g = input('введите число: ')
while not g.isdigit():
    g = input('я сказал число! введите число: ')
g = int(g)
gt1 = g % 10
gt2 = g // 10
grz = gt1
while not (gt2 == 0):
    gt1 = gt2 % 10
    gt2 = gt2 // 10
    if gt1 > grz:
        grz = gt1
print(grz)