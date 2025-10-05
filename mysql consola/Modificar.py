import mysql.connector

conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd2"
)

cursor1 = conexion1.cursor()
cursor1.execute("UPDATE articulos SET precio = 10 WHERE id = 16")
conexion1.commit()
conexion1.close()
print("Registro actualizado correctamente.")
