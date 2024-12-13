from database.db import connect_db
from models.report import Report
from controllers.commande_controller import CommandeController
import datetime


class ReportController:
    def __init__(self):
        self.connexion = connect_db()
        self.commande = CommandeController()


    def get_elements_report(self, prix_total=None):
        try:
            list_commande = []
            cursor = self.connexion.cursor()
            list_commande = cursor.execute("""
            SELECT * FROM Commande WHERE date BETWEEN %s AND %s
            """, (datetime.datetime.today(), datetime.datetime.today()))

            # Récuperation du nombre de commandes
            nbre_commandes = len(list_commande)
            if nbre_commandes == 0:
                return print("Aucune commande n'existe")
            
            # Récupération du chiffre d'affaire
            for commande in list_commande:
                prix_total += commande['prix_total']
        except Exception as e:
            print(e)






