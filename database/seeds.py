from mysql.connector import Error

def creer_tables(connexion):
    try:
        cursor = connexion.cursor()

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


        connexion.commit()
        print("Tables créées avec succès.")
    except Error as e:
        print(f"Erreur lors de la création des tables : {e}")

def inserer_data(connexion):
    try:
        cursor = connexion.cursor()

        # 1. Insérer des tables
        cursor.execute("INSERT IGNORE INTO TableResto (numero, est_occupée) VALUES (1, TRUE), (2, TRUE), (3, TRUE), (4, FALSE);")

        # 2. Insérer des plats (uniquement des burgers)
        cursor.execute("""
        INSERT IGNORE INTO Plat (nom, description) VALUES
        ('Cheeseburger', 'Burger classique avec fromage, salade et tomates'),
        ('Bacon Burger', 'Burger avec bacon, fromage, et sauce barbecue'),
        ('Vegan Burger', 'Burger végétalien avec galette de pois chiches et légumes');
        """)

        # 3. Insérer des ingrédients
        cursor.execute("""
        INSERT IGNORE INTO Ingredient (nom) VALUES
        ('Pain à burger'), 
        ('Steak haché'), 
        ('Fromage'), 
        ('Tomates'), 
        ('Salade'), 
        ('Bacon'), 
        ('Sauce barbecue'), 
        ('Galette de pois chiches'), 
        ('Cornichons'), 
        ('Oignons');
        """)

        # Récupérer les IDs des ingrédients insérés
        cursor.execute("SELECT id, nom FROM Ingredient;")
        ingredients = {nom: id for id, nom in cursor.fetchall()}

        # 4. Insérer des stocks
        cursor.execute("""
        INSERT IGNORE INTO Stock (ingredient_id, quantite) VALUES
        (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s);
        """, (
            ingredients['Pain à burger'], 50,
            ingredients['Steak haché'], 40,
            ingredients['Fromage'], 30,
            ingredients['Tomates'], 25,
            ingredients['Salade'], 20,
            ingredients['Bacon'], 15,
            ingredients['Sauce barbecue'], 10,
            ingredients['Galette de pois chiches'], 10,
            ingredients['Cornichons'], 15,
            ingredients['Oignons'], 20
        ))

        # 5. Insérer des commandes
        cursor.execute("""
        INSERT IGNORE INTO Commande (table_id, statut, montant, paye) VALUES
        (1, TRUE, 25.00, FALSE),
        (2, FALSE, 18.50, FALSE),
        (3, TRUE, 15.00, TRUE);
        """)

        # Récupérer les IDs des commandes insérées
        cursor.execute("SELECT id FROM Commande;")
        commandes = [row[0] for row in cursor.fetchall()]

        # 6. Lier des plats aux commandes
        cursor.execute("""
        INSERT IGNORE INTO plat_commande (plat_id, commande_id, quantite) VALUES
        ((SELECT id FROM Plat WHERE nom = 'Cheeseburger'), %s, 2),
        ((SELECT id FROM Plat WHERE nom = 'Bacon Burger'), %s, 1),
        ((SELECT id FROM Plat WHERE nom = 'Vegan Burger'), %s, 1);
        """, commandes)

        # Insérer les relations entre plats et ingrédients
        cursor.execute("""
        INSERT IGNORE INTO Plat_Ingredient (plat_id, ingredient_id) VALUES
        -- Cheeseburger
        ((SELECT id FROM Plat WHERE nom = 'Cheeseburger'), (SELECT id FROM Ingredient WHERE nom = 'Pain à burger')),
        ((SELECT id FROM Plat WHERE nom = 'Cheeseburger'), (SELECT id FROM Ingredient WHERE nom = 'Steak haché')),
        ((SELECT id FROM Plat WHERE nom = 'Cheeseburger'), (SELECT id FROM Ingredient WHERE nom = 'Fromage')),
        ((SELECT id FROM Plat WHERE nom = 'Cheeseburger'), (SELECT id FROM Ingredient WHERE nom = 'Tomates')),
        ((SELECT id FROM Plat WHERE nom = 'Cheeseburger'), (SELECT id FROM Ingredient WHERE nom = 'Salade')),

        -- Bacon Burger
        ((SELECT id FROM Plat WHERE nom = 'Bacon Burger'), (SELECT id FROM Ingredient WHERE nom = 'Pain à burger')),
        ((SELECT id FROM Plat WHERE nom = 'Bacon Burger'), (SELECT id FROM Ingredient WHERE nom = 'Steak haché')),
        ((SELECT id FROM Plat WHERE nom = 'Bacon Burger'), (SELECT id FROM Ingredient WHERE nom = 'Fromage')),
        ((SELECT id FROM Plat WHERE nom = 'Bacon Burger'), (SELECT id FROM Ingredient WHERE nom = 'Bacon')),
        ((SELECT id FROM Plat WHERE nom = 'Bacon Burger'), (SELECT id FROM Ingredient WHERE nom = 'Sauce barbecue')),

        -- Vegan Burger
        ((SELECT id FROM Plat WHERE nom = 'Vegan Burger'), (SELECT id FROM Ingredient WHERE nom = 'Pain à burger')),
        ((SELECT id FROM Plat WHERE nom = 'Vegan Burger'), (SELECT id FROM Ingredient WHERE nom = 'Galette de pois chiches')),
        ((SELECT id FROM Plat WHERE nom = 'Vegan Burger'), (SELECT id FROM Ingredient WHERE nom = 'Tomates')),
        ((SELECT id FROM Plat WHERE nom = 'Vegan Burger'), (SELECT id FROM Ingredient WHERE nom = 'Salade')),
        ((SELECT id FROM Plat WHERE nom = 'Vegan Burger'), (SELECT id FROM Ingredient WHERE nom = 'Cornichons')),
        ((SELECT id FROM Plat WHERE nom = 'Vegan Burger'), (SELECT id FROM Ingredient WHERE nom = 'Oignons'));
        """)

        # 7. Insérer des plats personnalisés
        cursor.execute("""
        INSERT IGNORE INTO custom_plat (nom) VALUES ('Double Bacon Burger');
        """)

        # Récupérer l'ID du plat personnalisé
        cursor.execute("SELECT id FROM custom_plat WHERE nom = 'Double Bacon Burger';")
        custom_plat_id = cursor.fetchone()[0]

        # Lier des ingrédients au plat personnalisé
        cursor.execute("""
        INSERT IGNORE INTO custom_plat_ingredient (custom_plat_id, ingredient_id) VALUES
        (%s, (SELECT id FROM Ingredient WHERE nom = 'Pain à burger')),
        (%s, (SELECT id FROM Ingredient WHERE nom = 'Steak haché')),
        (%s, (SELECT id FROM Ingredient WHERE nom = 'Fromage')),
        (%s, (SELECT id FROM Ingredient WHERE nom = 'Bacon')),
        (%s, (SELECT id FROM Ingredient WHERE nom = 'Sauce barbecue'));
        """, (custom_plat_id, custom_plat_id, custom_plat_id, custom_plat_id, custom_plat_id))

        # Lier le plat personnalisé à une commande
        cursor.execute("""
        INSERT IGNORE INTO custom_plat_commande (custom_plat_id, commande_id, quantite) VALUES
        (%s, %s, 1);
        """, (custom_plat_id, commandes[0]))

        connexion.commit()
        print("Données insérées avec succès.")
    except Error as e:
        print(f"Erreur lors de l'insertion des données : {e}")