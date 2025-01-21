import retrait
import depot
import consultersolde
from creercompte import creer_compte

def main():
    compte = creer_compte()
    if not compte:
        return

    nom = compte["nom"]
    mot_de_passe = compte["mot_de_passe"]
    solde = compte["solde"]

    while True:
        print("\nMenu principal")
        print("1. Consulter le solde")
        print("2. Faire un dépôt")
        print("3. Faire un retrait")
        print("4. Quitter")

        choix = input("Choisissez une opération (1-4) : ")

        if choix == "1":
            mot_de_passe_saisi = input("Entrez votre mot de passe : ")
            if mot_de_passe_saisi == mot_de_passe:
                print(consultersolde.consulter(solde))
            else:
                print("Mot de passe incorrect.")

        elif choix == "2":
            mot_de_passe_saisi = input("Entrez votre mot de passe : ")
            if mot_de_passe_saisi == mot_de_passe:
                try:
                    montant = float(input("Entrez le montant à déposer : "))
                    solde, message = depot.deposer(solde, montant)
                    print(message)
                except ValueError:
                    print("Montant invalide. Veuillez entrer un nombre.")
            else:
                print("Mot de passe incorrect.")

        elif choix == "3":
            mot_de_passe_saisi = input("Entrez votre mot de passe : ")
            if mot_de_passe_saisi == mot_de_passe:
                try:
                    montant = float(input("Entrez le montant à retirer : "))
                    solde, message = retrait.retirer(solde, montant)
                    print(message)
                except ValueError:
                    print("Montant invalide. Veuillez entrer un nombre.")
            else:
                print("Mot de passe incorrect.")

        elif choix == "4":
            print("Merci d'avoir utilisé notre service. À bientôt !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
