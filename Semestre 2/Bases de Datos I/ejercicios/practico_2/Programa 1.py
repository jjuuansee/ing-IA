import mysql.connector


def execute_query(query):
    # Conexión a la base de datos
    cnx = mysql.connector.connect(
        user='root',
        password='rootpassword',
        host='127.0.0.1',
        database='baseDatosI'
    )

    cursor = cnx.cursor()
    cursor.execute(query)

    resultado = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    cnx.close()


# Obtener todos los usuarios mayores de 18 años
query1 = """
SELECT nombreUsuario, nombre, apellido, 
       FLOOR(DATEDIFF(CURDATE(), fechaNacimiento) / 365) AS edad
FROM usuario
WHERE FLOOR(DATEDIFF(CURDATE(), fechaNacimiento) / 365) > 18;
"""

# Listar todos los pedidos hechos por un usuario en particular
query2 = """
SELECT idPedido, fechaSolicitud
FROM pedido
WHERE nombreUsuario = 'pperez';
"""

# Obtener el total gastado por cada usuario en sus pedidos
query3 = """
SELECT p.nombreUsuario, SUM(pp.cantidad * pr.precioUnitario) AS totalGastado
FROM pedido p
JOIN productoPedido pp ON p.idPedido = pp.idPedido
JOIN producto pr ON pp.idProducto = pr.idProducto
GROUP BY p.nombreUsuario;
"""

# Mostrar los productos más caros
query4 = """
SELECT nombreProducto, precioUnitario
FROM producto
ORDER BY precioUnitario DESC;
"""

# Obtener el número total de pedidos hechos por cada usuario
query5 = """
SELECT nombreUsuario, COUNT(idPedido) AS totalPedidos
FROM pedido
GROUP BY nombreUsuario;
"""

print("Consulta 1: Usuarios mayores de 18 años")
execute_query(query1)
print("\nConsulta 2: Pedidos de 'pperez'")
execute_query(query2)
print("\nConsulta 3: Total gastado por cada usuario")
execute_query(query3)
print("\nConsulta 4: Productos más caros")
execute_query(query4)
print("\nConsulta 5: Total de pedidos por usuario")
execute_query(query5)
