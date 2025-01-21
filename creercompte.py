def creer_compte():
    print("Création de compte bancaire")
    nom = input("Entrez votre nom : ")
    mot_de_passe = input("Créez un mot de passe : ")
    try:
        solde = float(input("Entrez le solde initial : "))
        if solde < 0:
            print("Le solde initial ne peut pas être négatif. Initialisation échouée.")
            return None
    except ValueError:
        print("Entrée invalide. Le solde doit être un nombre.")
        return None
    print(f"Compte créé avec succès pour {nom}.\n")
    return {"nom": nom, "mot_de_passe": mot_de_passe, "solde": solde}
