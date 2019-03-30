def is_prime(a):

    c1 = 0
    for x in range(1, n + 1):
        if n % x == 0:
            c1 = c1 + 1
    if c1 == 2:
        a=1
        print(a)
        return a
    else:
        a=0
        print(a)
        return a
n=1

while n>0:
    try:
        n = int(input("Introduce el número que quieres evaluar: "))
        is_prime(n)
    except ValueError:
        print(-1)
