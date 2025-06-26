from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO():
    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None: #controllare sempre che la connessione non sia None
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT c.codins 
                        FROM corso c"""

            cursor.execute(query)

            res = []
            for row in cursor:
                res.append(row["codins"])
            #processa res

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT * FROM corso c"""

            cursor.execute(query)

            res = []
            for row in cursor:
                # res.append(Corso(codins=row["codins"],
                #                  crediti = row["crediti"],
                #                  nome = row["nome"],
                #                  pd = row["pd"]))
                res.append(Corso(**row)) # faccio l'unpack del dizionario e lo passa al parametro con lo stesso nome
            # processa res

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT *
                        FROM corso c
                        WHERE c.pd = %s"""

            cursor.execute(query, (pd,))

            res = []
            for row in cursor:
                res.append(Corso(**row))

            cursor.close()
            cnx.close()
            return res


    @staticmethod
    def getCorsiPdWithIscritti(pd):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT c.codins, c.crediti, c.nome, c.pd, count(*) as n 
                        FROM corso c, iscrizione i
                        WHERE c.codins = i.codins
                        AND c.pd = %s
                        GROUP BY c.codins, c.crediti, c.nome, c.pd"""

            cursor.execute(query, (pd,))

            res = []
            for row in cursor:
                # restituiamo una tupla di corso e numero di iscritti
                res.append((Corso(row["codins"],
                                  row["crediti"],
                                  row["nome"],
                                  row["pd"]), row["n"])) #lista di tuple

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT s.*
                        FROM studente s, iscrizione i
                        WHERE s.matricola = i.matricola 
                        AND i.codins = %s"""

            cursor.execute(query, (codins,))

            res = []
            for row in cursor:
                res.append(Studente(**row))
                #che è equivalente alla riga successiva
                #res.append(Studente(row["matricola"], row["cognome"], row["nome"], row["cds"]))

            cursor.close()
            cnx.close()
            return res


    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """ SELECT s.CDS, count(*) as n
                        FROM studente s, iscrizione i
                        WHERE i.matricola = s.matricola
                        AND i.codins = %s
                        AND s.CDS != ""
                        GROUP BY s.CDS"""

            cursor.execute(query, (codins,))

            res = []
            for row in cursor:
                # restituiamo una lista di tuple, con corso di studio e numero studenti
                res.append((row["CDS"], row["n"]))

            cursor.close()
            cnx.close()
            return res

if __name__ == "__main__":
    print(DAO.getCodins())
    for c in DAO.getCorsiPdWithIscritti(1):
        print(c)