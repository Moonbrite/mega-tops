class CuisineController:

    @classmethod
    def showOrdersStatus(cls, connexion):
        cursor = connexion.cursor()
        cursor.execute("SELECT id FROM commande WHERE statut = %s", ("preparation",))
        results = cursor.fetchall()
        lst = []
        for result in results:
            commande_id = result[0]
            cursor.execute("""
                SELECT p.nom AS plat, cp.quantite AS quantite
                FROM plat_commande cp
                JOIN plat p ON cp.plat_id = p.id
                WHERE cp.commande_id = %s
            """, (commande_id,))
            plat = cursor.fetchall()

            lst.append({
                "commande_id": commande_id,
                "plats": plat
            })
        print("Commandes en préparation :")
        for commande in lst:
                print(f"\nCommande ID : {commande['commande_id']}")
                for plat in commande['plats']:
                    print(f"{plat[0]} : {plat[1]} unité(s)")