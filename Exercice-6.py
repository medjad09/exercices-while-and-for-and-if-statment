n = int(input("Entrez le nombre d'élèves dans la classe : "))

notes = []
somme = 0

for i in range(n):
    note = float(input(f"Entrez la note de l'élève {i + 1} : "))
    notes.append(note)
    somme += note

moyenne = somme / n

superieures_a_moyenne = [note for note in notes if note > moyenne]

print("Les notes supérieures à la moyenne sont :")
for note in superieures_a_moyenne:
    print(note)
