from database.db import connect_db

class Plat:
    def __init__(self, nom, description, prix):
        self.nom = nom
        self.description = description
        self.prix = prix

    def __str__(self):
        return f"Plat: {self.nom} - {self.description} - Prix: {self.prix}"

    def modifier_prix(self, nouveau_prix):
        self.prix = nouveau_prix

    def modifier_description(self, nouvelle_description):
        self.description = nouvelle_description
