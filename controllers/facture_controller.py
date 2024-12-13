
class FactureController:


    def print_facture(self,commande_id,connexion):

        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM plat_commande WHERE commande_id = %s;", (commande_id,))
        results = cursor.fetchall()
        prix_total = 0
        print("=======Commande===========\n")
        for result in results:
            cursor.execute("SELECT * FROM plat WHERE id = %s;", (result[2],))
            resu = cursor.fetchone()
            prix_total += resu[3]
            print(resu)
        print(f"Prix Total de la commande :{prix_total} € \n")
        print("==========================")