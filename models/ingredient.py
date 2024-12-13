from database.db import connect_db

class Ingredient:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"Ingrédient: {self.nom}"

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom
