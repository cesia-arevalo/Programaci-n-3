import mysql.connector

conexion1=mysql.connector.connect(host="localhost" ,
                                  user="root" ,
                                  passwd="" ,
                                  database="bd2")
cursor1=conexion1.cursor()
cursor1.execute("select id, descripcion, precio from articulos")
for datos in cursor1:
    print (datos)
conexion1.close()
print("Litos....")

