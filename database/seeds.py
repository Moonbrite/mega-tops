from db import connect_db
from mysql.connector import Error

def creer_tables():
    try:
        cnx = connect_db()

        cursor = cnx.cursor()

        # Table: TableResto
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS TableResto (
            id INT AUTO_INCREMENT PRIMARY KEY,
            numero INT NOT NULL UNIQUE,
            est_occupée BOOLEAN DEFAULT FALSE
        );
        """)

        # Table: Commande
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Commande (
            id INT AUTO_INCREMENT PRIMARY KEY,
            table_id INT NOT NULL,
            statut BOOLEAN DEFAULT FALSE,
            montant DOUBLE DEFAULT 0.0,
            paye BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (table_id) REFERENCES TableResto(id)
        );
        """)

        # Table: Plat
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Plat (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100) NOT NULL,
            description TEXT,
            prix DOUBLE NOT NULL
        );
        """)


        # Table: Plat_Commande
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Plat_Commande (
            id INT AUTO_INCREMENT PRIMARY KEY,
            commande_id INT NOT NULL,
            plat_id INT NOT NULL,
            quantite INT NOT NULL,
            FOREIGN KEY (commande_id) REFERENCES Commande(id),
            FOREIGN KEY (plat_id) REFERENCES Plat(id)
        );
        """)

        # Table: Custom_Plat
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Custom_Plat (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100) NOT NULL
        );
        """)

        # Table: Custom_Plat_Commande
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Custom_Plat_Commande (
            id INT AUTO_INCREMENT PRIMARY KEY,
            custom_plat_id INT NOT NULL,
            commande_id INT NOT NULL,
            quantite INT NOT NULL,
            FOREIGN KEY (custom_plat_id) REFERENCES Custom_Plat(id),
            FOREIGN KEY (commande_id) REFERENCES Commande(id)
        );
        """)

        # Table: Ingredient
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ingredient (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100) NOT NULL UNIQUE
        );
        """)

        # Table: Stock
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Stock (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ingredient_id INT NOT NULL,
            quantite INT DEFAULT 0 ,
            FOREIGN KEY (ingredient_id) REFERENCES Ingredient(id)
        );
        """)

        # Table: Plat_Ingredient
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Plat_Ingredient (
            id INT AUTO_INCREMENT PRIMARY KEY,
            plat_id INT NOT NULL,
            ingredient_id INT NOT NULL,
            FOREIGN KEY (plat_id) REFERENCES Plat(id),
            FOREIGN KEY (ingredient_id) REFERENCES Ingredient(id)
        );
        """)

        # Table: Custom_Plat_Ingredient
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Custom_Plat_Ingredient (
            id INT AUTO_INCREMENT PRIMARY KEY,
            custom_plat_id INT NOT NULL,
            ingredient_id INT NOT NULL,
            FOREIGN KEY (custom_plat_id) REFERENCES Custom_Plat(id),
            FOREIGN KEY (ingredient_id) REFERENCES Ingredient(id)
        );
        """)


        cnx.commit()
        print("Tables créées avec succès.")
    except Error as e:
        print(f"Erreur lors de la création des tables : {e}")

creer_tables()