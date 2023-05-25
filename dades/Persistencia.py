import mysql.connector
from dades.Database import Database

class Persistencia:

    @staticmethod
    def eliminar_mesures(nom):
        with Database() as db:
            sql = "DELETE FROM mesura WHERE nom=%s"
            val = [nom]        
            db.execute(sql,val)    
            db.commit()

    @staticmethod
    def afegir_mesura(nom,x,y):
        with Database() as db:
            sql = "INSERT INTO mesura (nom, x, y) VALUES (%s, %s, %s)"
            val = [nom,x,y]
            db.execute(sql, val)    
            db.commit()

    @staticmethod
    def obtenir_mesures(nom):
        data=[]
        with Database() as db:
            sql = "SELECT * FROM mesura WHERE nom=%s"
            val = [nom]
            db.execute(sql, val)
            row = db.fetchone()   
            while row!=None:
                data.append(row)
                row = db.fetchone()    
        return data

    @staticmethod
    def obtenir_ultima_mesura(nom):
        row=None
        with Database() as db:
            sql = "SELECT * FROM mesura WHERE nom=%s ORDER BY data DESC LIMIT 1"
            val = [nom]
            db.execute(sql, val)
            row = db.fetchone()       
        return row


