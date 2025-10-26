import mysql.connector


class Mascotas:

    def abrir(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="hola_mundo1"
        )
        return conexion

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO mascotas (Name, Species, Sex, Birth) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT Name, Species, Sex, Birth FROM mascotas WHERE PetID = %s"
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        cone.close()
        return resultado

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT PetID, Name, Species FROM mascotas"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cone.close()
        return resultado

    def baja(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM mascotas WHERE PetID = %s"
        cursor.execute(sql, datos)
        cone.commit()
        afectados = cursor.rowcount
        cone.close()
        return afectados

    def modificacion(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "UPDATE mascotas SET Name = %s, Species = %s, Sex = %s, Birth = %s WHERE PetID = %s"
        cursor.execute(sql, datos)
        cone.commit()
        afectados = cursor.rowcount
        cone.close()
        return afectados