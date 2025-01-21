def deposer(solde, montant):
    if montant <= 0:
        return solde, "Dépôt impossible : le montant doit être supérieur à 0."
    solde += montant
    return solde, f"Dépôt de {montant} éffectué avec succès. Nouveau solde : {solde}"