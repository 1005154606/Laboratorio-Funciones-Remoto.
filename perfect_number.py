n=int(input("Introduce el número: "))
acd=0
for x in range(1,n):
    if n%x==0:
        acd=acd+x
if acd==n:
    print("El número es perfecto")
else:
    print("El número no es perfecto")

