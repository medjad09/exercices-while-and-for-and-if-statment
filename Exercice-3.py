M = int(input("Entrez un premier entier M : "))
N = int(input("Entrez un deuxième entier N : "))

somme_diviseurs_M = 0
for i in range(2, M):
    if M % i == 0:
        somme_diviseurs_M += i

somme_diviseurs_N = 0
for i in range(2, N):
    if N % i == 0:
        somme_diviseurs_N += i

if somme_diviseurs_M == N and somme_diviseurs_N == M:
    print(f"{M} et {N} sont des amis.")
else:
    print(f"{M} et {N} ne sont pas amis.")
