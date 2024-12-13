import mysql.connector
from mysql.connector import Error


def connect_db():
    try:
        cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            port=3306,
            database="restaurant"
        )

        if cnx.is_connected():
            print("Connexion réussie à la base de données !")

        return cnx

    except Error as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
        return None
