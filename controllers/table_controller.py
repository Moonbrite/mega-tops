from models.table import Table


class Table_controller:

    def __init__(self):
        self.tables = [Table(i) for i in range(1, 5)]

    def update_table(self, connexion):

        try:
            cursor = connexion.cursor()
            self.get_all_table(connexion)
            num_table = self.get_table_number()

            # Vérifier si la table existe et est disponible
            cursor.execute("SELECT est_occupée FROM TableResto WHERE numero = %s;", (num_table,))
            result = cursor.fetchone()

            est_occupee = result[0]
            if est_occupee:
                print(f"La table numéro {num_table} est déjà occupée.")
                return


            cursor.execute("UPDATE TableResto SET est_occupée = TRUE WHERE numero = %s;", (num_table,))
            connexion.commit()
            print(f"La table numéro {num_table} est maintenant occupée.")
            return num_table
        except Exception as e:
            print(f"Erreur lors de la mise à jour de la table : {e}")

    def get_table_number(self):

        while True:
            try:
                num_table = int(input("Veuillez entrer le numéro de la table : "))
                if num_table > 0:
                    return num_table

            except ValueError:
                print("Veuillez entrer un numéro valide.")

    def get_all_table(self,connexion):
        cursor = connexion.cursor()

        cursor.execute("SELECT numero FROM TableResto WHERE est_occupée = FALSE;")
        tables_disponibles = cursor.fetchall()
        print(f"Tables disponibles : {[table[0] for table in tables_disponibles]}")

