from database.db import connect_db

class Commande:
    def __init__(self, table_id, statut=False, montant=0.0, paye=False):
        self.table_id = table_id
        self.statut = statut
        self.montant = montant
        self.paye = paye

    def __str__(self):
        return f"Commande pour table {self.table_id} - Statut: {'Prête' if self.statut else 'En cours'} - Montant: {self.montant} - Payé: {'Oui' if self.paye else 'Non'}"

    def marquer_comme_paye(self):
        self.paye = True

    def changer_statut(self, statut):
        self.statut = statut
