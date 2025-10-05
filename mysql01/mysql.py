import mysql.connector

class Articulos:
    def abrir(self):
        conexion=mysql.connector.connect(host="localhost",
                                         user="root",
                                         passwd="",
                                         database="ugb01")
        return conexion
    def guardar(self, datos):
        cone = self.abrir()
        cursor=cone.cursor()
        sql="insert into productos(nombre, precio) values (%s, %s)"
        cursor.execute(sql,datos)
        cone.conmit()
        cone.close()


        def consulta(self, datos):
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "select nombre, precio from productos where codigo=%s"
            cursor.execute(sql, datos)
            cone.close()
            return cursor.fefchall()

        def recuperar_todos(self):
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "select nombre, precio from productos"
            cursor.execute(sql)
            cone.close()
            return cursor.fefchall()

        def baja(self, datos):
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "delete from productos where codigo=%s"
            cursor.execute(sql,datos)
            cone.close()
            return cursor.rowcount()#retorna la cantidad de filas afectadas

        def modificacion(self, datos):
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "update productos set nombre=%s, precio=%s where codigo=%s"
            cursor.execute(sql, datos)
            cone.close()
            return cursor.rowcount()