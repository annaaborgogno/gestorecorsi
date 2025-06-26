from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPd(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPdWithIscritti(self, pd):
        return DAO.getCorsiPdWithIscritti(pd)

    def getStudentiCorsi(self, codins):
        # li stampo in ordine di cognome
        studenti = DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda s: s.cognome) #lambda è un costrutto per definire una funzione senza nome
        return studenti

    def getCDSofCorso(self, codins):
        # ordiniamo i corsi per numero di studenti iscritti in modo decrescente
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key=lambda c: c[1], reverse=True)
        return cds