def a_power_b(a,b):
    prod=1

    for x in range(0,b):
        prod=prod*a




    if a>1000 or b>1000:
        raise NameError('El número es demasiado grande')




    return prod
contpotencias=0
contpar=0
contimpar=0
conterror=1
try:
    x=int(input("Introduce la base: "))
    y=int(input("Introduce el exponente: "))
    a_power_b(x,y)
    z = a_power_b(x, y)
    print(z)
    contpotencias = contpotencias + 1
    if z%2==0:
        contpar=contpar+1
    else:
        contimpar=contimpar+1






    while x>0:
        x = int(input("Introduce la base: "))
        if x==0:
            break
        y = int(input("Introduce el exponente: "))
        a_power_b(x, y)
        c= a_power_b(x, y)
        print(c)
        contpotencias=contpotencias+1
        if z % 2 == 0:
            contpar = contpar + 1
        else:
            contimpar = contimpar + 1






except ValueError:

    print("Error")

print("Hubieron",contpotencias,"resultados")
print("Hubieron",contpar,"resultados pares")
print("Hubieron", contimpar,"resultados impares")
