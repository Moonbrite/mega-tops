from controllers.table_controller import Table_controller
from database.db import connect_db
from database.seeds import creer_tables, inserer_data


def afficher_menu_principal():
    print("\n--- Système de Gestion du Restaurant ---")
    print("1. Gérer les tables")
    print("2. Gérer les commandes")
    print("3. Gérer le stock")
    print("4. Quitter")
    return input("Choisissez une option : ")

def switch_action(action,connexion):
    match action:
        case "1":
            table_controller = Table_controller()
            table_controller.update_table(connexion)


def main():
    connexion = connect_db()

    if connexion:
        creer_tables(connexion)
        inserer_data(connexion)

        switch_action(afficher_menu_principal(),connexion)
        connexion.close()



if __name__ == "__main__":
    main()


    