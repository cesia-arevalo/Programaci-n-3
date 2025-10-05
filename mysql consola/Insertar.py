import mysql.connector

conexion1=mysql.connector.connect(host="localhost" ,
                                  user="root" ,
                                  passwd="" ,
                                  database="bd2")
cursor1=conexion1.cursor()
sql="insert into articulos(descripcion, precio) values (%s ,%s)"
datos=("Raton" , 3)
cursor1.execute(sql, datos)
datos=("Teclado" , 7)
cursor1.execute(sql, datos)
datos=("Monitor" , 5)
cursor1.execute(sql, datos)
datos=("pollo" , 1)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()
print("se han guardado")