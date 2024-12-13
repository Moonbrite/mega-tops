from database.db import connect_db

class Table:
    def __init__(self, numero, est_occupee=False):
        self.numero = numero
        self.est_occupee = est_occupee

    def __str__(self):
        return f"Table {self.numero} - {'Occupée' if self.est_occupee else 'Libre'}"

    def changer_etat(self, est_occupee):
        self.est_occupee = est_occupee
