import datetime

class Report():
    def __init__(self, date, chiffre_d_affaire, nbre_commandes, list_commande):
        self.date = datetime.datetime.strptime(date, "%d-%m-%Y")
        self.chiffre_d_affaire = chiffre_d_affaire
        self.nbre_commandes = nbre_commandes
        self.list_commande = list_commande

    list_commande = []

    def __str__(self):
        return f"Sur la date: {self.date.strftime('%d/%m/%Y')}- Nous avons eu {self.nbre_commandes} commandes avec {self.chiffre_d_affaire} - Voici les commandes{self.list_commande}"
