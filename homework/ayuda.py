import sqlite3

# Ruta a los archivos SQL
create_tables_file = 'tests/create_tables.sql'
pregunta_08_file = 'homework/pregunta_13.sql'

# Función para leer y ejecutar un archivo SQL
def execute_sql_file(connection, file_path):
    with open(file_path, 'r') as file:
        sql = file.read()
        cursor = connection.cursor()
        cursor.executescript(sql)
        connection.commit()

# Conexión a la base de datos (SQLite como ejemplo)
conn = sqlite3.connect(':memory:')  # Usa ':memory:' para una base de datos en memoria

try:
    # Ejecutar el script de creación de tablas y llenado
    execute_sql_file(conn, create_tables_file)

    # Leer y ejecutar el archivo de consulta
    with open(pregunta_08_file, 'r') as file:
        query = file.read()
        cursor = conn.cursor()
        cursor.execute(query)

        # Obtener y mostrar resultados
        results = cursor.fetchall()
        for row in results:
            print(row)
finally:
    conn.close()