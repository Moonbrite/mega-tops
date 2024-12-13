from database.db import connect_db
from database.seeds import creer_tables, inserer_data


def afficher_menu_principal():
    print("\n--- Système de Gestion du Restaurant ---")
    print("1. Gérer les tables")
    print("2. Gérer les commandes")
    print("3. Gérer le stock")
    print("4. Quitter")
    return input("Choisissez une option : ")

def main():
    connexion = connect_db()

    if connexion:
        creer_tables(connexion)
        inserer_data(connexion)
        afficher_menu_principal()
        connexion.close()



if __name__ == "__main__":
    main()


    