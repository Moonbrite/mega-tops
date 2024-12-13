from controllers.table_controller import Table_controller
from controllers.commande_controller import CommandeController
from controllers.plat_controller import PlatController
from database.db import connect_db
from database.seeds import creer_tables, inserer_data


def afficher_menu_principal():
    print("\n--- Système de Gestion du Restaurant ---")
    print("1. Gérer les tables")
    print("2. Gérer les commandes")
    print("3. Gérer le stock")
    print("4. Quitter")
    return input("Choisissez une option : ")


def switch_action(action, connexion):
    match action:
        case "1":
            table_controller = Table_controller()
            table_controller.update_table(connexion)
        case "2":
            commande_controller = CommandeController()
            plat_controller = PlatController()
            table_controller = Table_controller()
            try:
                table_controller.get_all_table(connexion)
                table_id = table_controller.get_table_number()
                commande_id = commande_controller.creer_commande(table_id)
                if commande_id:
                    plats = plat_controller.get_all_plats()
                    plat_map = {index + 1: plat for index, plat in enumerate(plats)}
                    print("\nVeuillez choisir un plat :")
                    while True:
                        try:
                            choix = int(input("\nEntrez le numéro du plat souhaité : "))
                            if choix in plat_map:
                                plat_id = plat_map[choix][0]
                                break
                            else:
                                print("Choix invalide. Veuillez sélectionner un numéro dans la liste.")
                        except ValueError:
                            print("Veuillez entrer un numéro valide.")

                    quantite = int(input("Entrez la quantité : "))
                    commande_controller.ajouter_plat_a_commande(commande_id, plat_id, quantite)
                else:
                    print("Erreur lors de la création de la commande.")

            except ValueError:
                print("Entrée invalide. Veuillez réessayer.")


def main():
    connexion = connect_db()

    if connexion:
        # creer_tables(connexion)
        # inserer_data(connexion)
        switch_action(afficher_menu_principal(), connexion)
        connexion.close()


if __name__ == "__main__":
    main()
