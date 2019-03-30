n=int(input("Introduce el número: "))
acd=0
for x in range(1,n):
    if n%x==0:
        acd=acd+x
resta=acd-n
print(resta)
if resta<=3 and resta>=-3:
    print("El número es casi perfecto")
else:
    print("El número no es casi perfecto")

