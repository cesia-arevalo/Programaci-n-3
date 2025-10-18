import mysql.connector

class Empleados:
    def abrir(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd1"  # Cambia si tu base tiene otro nombre
        )
        return conexion

    def alta(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = """INSERT INTO empleados 
                 (nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()

    def consulta(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = """SELECT nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas 
                 FROM empleados WHERE empleado_id = %s"""
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        conexion.close()
        return resultado

    def baja(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = "DELETE FROM empleados WHERE empleado_id = %s"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()

    def modificacion(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        sql = """UPDATE empleados 
                 SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, email=%s, 
                     fecha_contrato=%s, notas=%s 
                 WHERE empleado_id=%s"""
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()
