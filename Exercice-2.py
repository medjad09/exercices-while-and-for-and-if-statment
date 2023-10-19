n = int(input("Entrez un entier : "))
diviseurs = []

for i in range(1, n + 1):
    if n % i == 0:
        diviseurs.append(i)

print(f"Les diviseurs de {n} sont : {diviseurs}")
print(f"Nombre de diviseurs trouvés : {len(diviseurs)}")
