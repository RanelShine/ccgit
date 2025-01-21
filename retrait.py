def retirer(solde, montant):
    if montant > solde:
        return solde, f"Retrait impossible : fonds insuffisants. Solde actuel : {solde}"
    solde -= montant
    return solde, f"Retrait de {montant} éffectué avec succès. Nouveau solde : {solde}"