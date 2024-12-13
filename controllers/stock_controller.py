from models.stock import Stock

class StockController:

    def __init__(self):
        self.stock = Stock

    @classmethod
    def showStock(cls, connexion):
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM ingredient")
        results = cursor.fetchall()
        for stock in results:
            print("------------------------------------------------------")
            print(f"Ingrédient : {stock[1]} -- Quantité : {stock[2]}")

    @classmethod
    def updateStock(cls, connexion, commande_id):
        cursor = connexion.cursor()
        # Étape 1 : Récupérer les plats et quantités de la commande
        cursor.execute("""
            SELECT plat_id, quantite 
            FROM plat_commande 
            WHERE commande_id = %s
        """, (commande_id,))
        plats_commande = cursor.fetchall()

        # Étape 2 : Calculer les ingrédients nécessaires
        for plat_id, quantite_plats in plats_commande:
            # Récupérer les ingrédients nécessaires pour le plat
            cursor.execute("""
                SELECT ingredient_id
                FROM plat_ingredient
                WHERE plat_id = %s
            """, (plat_id,))
            ingredients_plat = cursor.fetchall()

            # Réduire le stock pour chaque ingrédient
            for ingredient_id in ingredients_plat:
                cursor.execute("""
                    UPDATE ingredient
                    SET quantite = quantite - %s
                    WHERE id = %s
                """, (quantite_plats, ingredient_id[0]))
        connexion.commit()
        print(f"Stock mis à jour pour la commande {commande_id}.")