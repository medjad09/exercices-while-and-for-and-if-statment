N = int(input("Entrez la taille des tableaux T1 et T2 : "))

T1 = []
T2 = []
T = []

print("Entrez les éléments du tableau T1 :")
for i in range(N):
    valeur = int(input(f"T1[{i}]: "))
    T1.append(valeur)

print("Entrez les éléments du tableau T2 :")
for i in range(N):
    valeur = int(input(f"T2[{i}]: "))
    T2.append(valeur)

for i in range(N):
    somme = T1[i] + T2[i]
    T.append(somme)

print("Tableau T (somme de T1 et T2) :")
for i in range(N):
    print(f"T[{i}] = {T[i]}")
