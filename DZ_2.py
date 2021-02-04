b = input('введите число секунд: ')
while not b.isdigit():
    b = input('я сказал число! введите число секунд: ')
b = int(b)
#print(b//3600)
c1 = b//3600
c2 = (b-c1*3600)//60
c3 = b-c1*3600-c2*60
print(c1,':',c2,':',c3)