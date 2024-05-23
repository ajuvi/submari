import mysql.connector
from dades.Database import Database

class Persistencia:

    @staticmethod
    def eliminar_mesures(nom):
        try:
            with Database() as db:
                sql = "DELETE FROM mesura WHERE nom=%s"
                val = [nom]        
                db.execute(sql,val)    
                num = db.affected_rows()
                db.commit()
                return num
        except:
            print('ERROR en Persistencia.eliminar_mesures')
            raise

    @staticmethod
    def afegir_mesura(nom,x,y):
        try:
            with Database() as db:
                sql = "INSERT INTO mesura (nom, x, y) VALUES (%s, %s, %s)"
                val = [nom,x,y]
                db.execute(sql, val)    
                db.commit()
        except:
            print('ERROR en Persistencia.afegir_mesura')
            raise

    @staticmethod
    def obtenir_mesures(nom):        
        try:
            with Database() as db:
                data=[]
                sql = "SELECT * FROM mesura WHERE nom=%s"
                val = [nom]
                db.execute(sql, val)
                row = db.fetchone()   
                while row!=None:
                    data.append(row)
                    row = db.fetchone()    
                return data
        except:
            print('ERROR en Persistencia.obtenir_mesures')
            raise

    @staticmethod
    def obtenir_ultima_mesura(nom):
        
        try:            
            with Database() as db:
                sql = "SELECT * FROM mesura WHERE nom=%s ORDER BY data DESC LIMIT 1"
                val = [nom]
                db.execute(sql, val)
                row = db.fetchone()
                return row
        except:
            print('ERROR en Persistencia.obtenir_mesures')
            raise