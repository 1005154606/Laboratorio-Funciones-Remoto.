def a_power_b(a,b):
    prod=1

    for x in range(0,b):
        prod=prod*a

    print(prod)
    return prod

x=int(input("Introduce la base: "))
y=int(input("Introduce el exponente: "))
a_power_b(x,y)

while x>0:
    x = int(input("Introduce la base: "))
    if x==0:
        break
    y = int(input("Introduce el exponente: "))
    a_power_b(x, y)

