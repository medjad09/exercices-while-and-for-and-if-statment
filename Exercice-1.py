n = int(input("Entrez un entier n : "))
print(f"Nombres premiers inférieurs à {n}:")

if n > 1:
    for num in range(2, n):
        est_premier = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                est_premier = False
                break
        if est_premier:
            print(num)
else:
    print("Aucun nombre premier inférieur à", n)
