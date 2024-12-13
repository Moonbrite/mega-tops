from database.db import connect_db

class Stock:
    def __init__(self, ingredient_id, quantite):
        self.ingredient_id = ingredient_id
        self.quantite = quantite

    def __str__(self):
        return f"Ingrédient {self.ingredient_id} - Quantité: {self.quantite}"

    def ajouter_quantite(self, quantite):
        self.quantite += quantite

    def retirer_quantite(self, quantite):
        if self.quantite >= quantite:
            self.quantite -= quantite
        else:
            raise ValueError("Quantité insuffisante en stock.")
