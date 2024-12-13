from models.commande import Commande
from database.db import connect_db
from controllers.stock_controller import StockController

class CommandeController:
    def __init__(self):
        self.connexion = connect_db()
        self.stock_controller = StockController()

    def creer_commande(self, table_id):
        try:
            cursor = self.connexion.cursor()
            cursor.execute(
                """
                INSERT INTO Commande (table_id, statut, montant, paye)
                VALUES (%s, FALSE, 0.0, FALSE)
                """,
                (table_id,)
            )
            self.connexion.commit()
            print("Commande créée avec succès.")
            return cursor.lastrowid  
        except Exception as e:
            print(f"Erreur lors de la création de la commande : {e}")
            return None

    def ajouter_plat_a_commande(self, commande_id, plat_id, quantite):
        try:
            cursor = self.connexion.cursor()
            cursor.execute("""
                INSERT INTO Plat_Commande (commande_id, plat_id, quantite)
                VALUES (%s, %s, %s);
            """, (commande_id, plat_id, quantite))
            self.connexion.commit()
            print(f"Plat ajouté.")
        except Exception as e:
            print(f"Erreur lors de l'ajout du plat à la commande : {e}")
