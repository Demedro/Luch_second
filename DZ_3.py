d = input('введите число: ')
while not d.isdigit():
    d = input('я сказал число! введите число: ')
d1 = int(d)
d2 = int(d + d)
d3 = int(d + d + d)
print(d1 + d2 + d3)