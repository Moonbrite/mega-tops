

def afficher_menu_principal():
    print("\n--- Système de Gestion du Restaurant ---")
    print("1. Gérer les tables")
    print("2. Gérer les commandes")
    print("3. Gérer le stock")
    print("4. Quitter")
    return input("Choisissez une option : ")

def main():
    # Initialisation des contrôleurs
    afficher_menu_principal()
    return


if __name__ == "__main__":
    main()