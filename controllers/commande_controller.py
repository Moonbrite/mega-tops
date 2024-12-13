from models.commande import Commande
from database.db import connect_db
from controllers.stock_controller import StockController


class CommandeController:
    def __init__(self):
        self.stock_controller = StockController()

    def creer_commande(self, connexion, table_id):
        try:
            cursor = connexion.cursor()
            cursor.execute(
                """
                INSERT INTO Commande (table_id, statut, montant, paye)
                VALUES (%s, FALSE, 0.0, FALSE)
                """,
                (table_id,)
            )
            connexion.commit()
            print("Commande créée avec succès.")
            return cursor.lastrowid
        except Exception as e:
            print(f"Erreur lors de la création de la commande : {e}")
            return None

    def ajouter_plat_a_commande(self, connexion, commande_id, plat_id, quantite):
        try:
            cursor = connexion.cursor()
            cursor.execute("""
                INSERT INTO Plat_Commande (commande_id, plat_id, quantite)
                VALUES (%s, %s, %s);
            """, (commande_id, plat_id, quantite))
            connexion.commit()
            print(f"Plat ajouté.")
        except Exception as e:
            print(f"Erreur lors de l'ajout du plat à la commande : {e}")

    def mettre_a_jour_montant(self,connexion, commande_id, montant):
        try:
            cursor = connexion.cursor()
            cursor.execute("""
                UPDATE Commande
                SET montant = %s
                WHERE id = %s;
            """, (montant, commande_id))
            connexion.commit()
            print(f"Montant total mis à jour : {montant} €")
        except Exception as e:
            print(f"Erreur lors de la mise à jour du montant : {e}")

    def mettre_a_jour_statut(self,connexion, commande_id, statut):
        try:
            cursor = connexion.cursor()
            cursor.execute("""
                UPDATE Commande
                SET statut = %s
                WHERE id = %s;
            """, (statut, commande_id))
            connexion.commit()
            print(f"Statut de la commande {commande_id} mis à jour : {statut}")
        except Exception as e:
            print(f"Erreur lors de la mise à jour du statut : {e}")
