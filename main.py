from controllers.cuisine_controller import CuisineController
from controllers.stock_controller import StockController
from controllers.table_controller import Table_controller
from controllers.commande_controller import CommandeController
from controllers.plat_controller import PlatController
from controllers.facture_controller import FactureController
from database.db import connect_db
from database.seeds import creer_tables, inserer_data


def afficher_menu_principal():
    print("\n--- Système de Gestion du Restaurant ---")
    print("1. Voir les tables")
    print("2. Gérer les commandes")
    print("3. Affichage Cuisine")
    print("4. Quitter")
    return input("Choisissez une option : ")


def switch_action(action, connexion):
    if action == "1":
        Table_controller().get_all_table(connexion)
    elif action == "2":
        gerer_commande(connexion)
    elif action == "3":
        CuisineController().showOrdersStatus(connexion)
    elif action == "4":
        print("Merci d'avoir utilisé le système. À bientôt !")
        return False  # Arrête la boucle
    else:
        print("Choix invalide. Veuillez réessayer.")
    return True


def gerer_commande(connexion):
    commande_controller = CommandeController()
    plat_controller = PlatController()
    facture_controller = FactureController()
    table_controller = Table_controller()
    stock_controller = StockController()
    try:
        table_id = table_controller.update_table(connexion)
        commande_id = commande_controller.creer_commande(connexion, table_id)
        if commande_id:
            plats = plat_controller.get_all_plats()
            plat_map = {index + 1: plat for index, plat in enumerate(plats)}
            while True:
                print("\nVeuillez choisir un plat :")
                try:
                    choix = int(input("\nEntrez le numéro du plat souhaité : "))
                    if choix in plat_map:
                        plat_id = plat_map[choix][0]
                        quantite = int(input("Entrez la quantité : "))
                        commande_controller.ajouter_plat_a_commande(connexion, commande_id, plat_id, quantite)
                    else:
                        print("Choix invalide. Veuillez sélectionner un numéro dans la liste.")
                        continue
                except ValueError:
                    print("Veuillez entrer un numéro valide.")
                    continue

                ajouter_autre = input("Voulez-vous ajouter un autre plat ? (oui/non) : ").strip().lower()
                if ajouter_autre != "oui":
                    statut_commande = "en preparation"
                    montant_total = facture_controller.montant_total(commande_id, connexion)
                    commande_controller.mettre_a_jour_montant(connexion, commande_id, montant_total)
                    commande_controller.mettre_a_jour_statut(connexion, commande_id, statut_commande)
                    stock_controller.updateStock(connexion, commande_id)
                    print(f"Commande envoyée en cuisine !\nMontant total : {montant_total} €")
                    break
        else:
            print("Erreur lors de la création de la commande.")
    except ValueError:
        print("Entrée invalide. Veuillez réessayer.")

def main():
    connexion = connect_db()

    if connexion:
        # creer_tables(connexion)
        # inserer_data(connexion)
        while True:
            action = afficher_menu_principal()
            continuer = switch_action(action, connexion)
            if not continuer:
                break
        connexion.close()


if __name__ == "__main__":
    main()
