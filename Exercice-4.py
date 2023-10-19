mot_de_passe = "DEV@2023"
tentatives_restantes = 3

while tentatives_restantes > 0:
    entree = input("Veuillez entrer le mot de passe : ")
    if entree == mot_de_passe:
        print("Bonjour")
        break
    else:
        tentatives_restantes -= 1
        if tentatives_restantes > 0:
            print(f"Mot de passe incorrect. Il vous reste {tentatives_restantes} tentatives.")
        else:
            question_secrete = input("Mot de passe incorrect. Veuillez répondre à la question secrète (par exemple, votre film préféré) : ")
            if question_secrete.lower() == "votre film préféré":  # Remplacez par votre question secrète réelle
                print("Bonjour")
            else:
                print("Accès refusé. La réponse à la question secrète est incorrecte.")
