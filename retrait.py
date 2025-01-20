class CompteBancaire:
    def __init__(self, nom_titulaire, mot_de_passe, solde_initial=0):
        self.nom_titulaire = nom_titulaire
        self.mot_de_passe = mot_de_passe
        self.solde = solde_initial

    def deposer(self, montant, mot_de_passe):
        #Ajoute un montant au solde du compte.
        if mot_de_passe != self.mot_de_passe:
            print("Mot de passe incorrect.")
            return
        
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant} effectué. Nouveau solde: {self.solde}")
        else:
            print("Le montant à déposer doit être positif.")

    def retirer(self, montant, mot_de_passe):
        # Retire un montant du solde du compte
        if mot_de_passe != self.mot_de_passe:
            print("Mot de passe incorrect.")
            return
        
        if montant <= 0:
            print("Le montant à retirer doit être positif.")
        elif montant > self.solde:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde: {self.solde}")

    def afficher_solde(self, mot_de_passe):
       #Affiche le solde actuel du compte
        if mot_de_passe != self.mot_de_passe:
            print("Mot de passe incorrect.")
            return
        
        print(f"Solde actuel de {self.nom_titulaire}: {self.solde}")

def demander_montant(operation):
    # """Demande un montant valide à l'utilisateur
    
    while True:
        try:
            montant = float(input(f"Entrez le montant à {operation} : "))
            if montant <= 0:
                print("Le montant doit être positif. Veuillez réessayer.")
            else:
                return montant
        except ValueError:
            print("Entrée invalide. Veuillez entrer un montant en chiffres.")

# Fonction principale pour interagir avec l'utilisateur
def main():
    nom = input("Entrez le nom du titulaire du compte : ")
    mot_de_passe = input("Entrez un mot de passe : ")
    solde_initial = float(input("Entrez le solde initial : "))
    
    compte = CompteBancaire(nom, mot_de_passe, solde_initial)

    while True:
        print("\nMenu :")
        print("1. Afficher le solde")
        print("2. Déposer de l'argent")
        print("3. Retirer de l'argent")
        print("4. Quitter")
        
        choix = input("Choisissez une option (1-4) : ")

        mot_de_passe_entree = input("Entrez le mot de passe : ")

        if choix == "1":
            compte.afficher_solde(mot_de_passe_entree)
        elif choix == "2":
            montant = demander_montant("déposer")
            compte.deposer(montant, mot_de_passe_entree)
        elif choix == "3":
            montant = demander_montant("retirer")
            compte.retirer(montant, mot_de_passe_entree)
        elif choix == "4":
            print("Merci d'avoir utilisé le système!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Exécution de la fonction principale
if __name__ == "__main__":
    main()