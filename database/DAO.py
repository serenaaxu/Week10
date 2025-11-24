from database.DB_connect import DBConnect
from Connessione import Connessione

class DAO():
    pass

    @staticmethod
    def readAllFermate():
        # prendere una connessione dal DB connect
        conn = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM Fermata" # leggere tutte le informazioni dalla tabella fermata
        cursor = conn.cursor(dictionary=True)

        cursor.execute(query)
        for row in cursor:
            fermata = Fermata(row["id_fermata"], row["nome"])
            result.append(fermata)
            result.append(row)  # non ho parametri, quindi non serve passarli
            print(row)

        cursor.close()
        conn.close()
        return result # restituisco lista di oggetti

    @staticmethod
    def existsConnessioneTra(u : Fermata, v : Fermata):
        conn = DBConnect.get_connection()


    @staticmethod
    def searchViciniAFermata(u: Fermata):
        conn = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM connessione c WHERE c.id_stazP = %s"

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (u.id_fermata,)) # parametro con (, )
        for row in cursor:
            connessione = Connessione(row["id_connessione"], row["id_linea"], row["id_stazP"]), row["id_stazA"]
            result.append(connessione)
            result.append(row)
            print(row)
        cursor.close()
        conn.close()
        return result
