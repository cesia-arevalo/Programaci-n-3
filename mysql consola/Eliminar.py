import mysql.connector
conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd2"
)

cursor1 = conexion1.cursor()
cursor1.execute("DELETE FROM articulos WHERE id = 20")

conexion1.commit()
conexion1.close()
print("Registro eliminado.")
