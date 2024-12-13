from database.db import connect_db

class PlatController:
    def __init__(self):
        self.connexion = connect_db()

    def get_all_plats(self):
        try:
            cursor = self.connexion.cursor()
            cursor.execute("SELECT id, nom, description, prix FROM Plat;")
            plats = cursor.fetchall()
            print("Plats disponibles :")
            for plat in plats:
                print(f"[{plat[0]}] {plat[1]} - {plat[2]} - {plat[3]:.2f}€")
            return plats
        except Exception as e:
            print(f"Erreur lors de la récupération des plats : {e}")
            return []
        
