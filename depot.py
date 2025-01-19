class depot:
    def __init__(self, solde:float):
        self.solde=solde
    def deposer(self,depot: float):
        self.solde += depot
        return self.solde

        