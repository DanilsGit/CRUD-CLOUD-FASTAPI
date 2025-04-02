import psycopg2

try:
    conn = psycopg2.connect(
        host="database-2.c7oaweysscze.us-west-1.rds.amazonaws.com",
        port=5432,
        user="postgres",
        password="eSZDeWtKbxHyR3tW99eg",
        database="postgres"  # ¡Usa la BD predeterminada!
    )
    print("¡Conexión exitosa!")
    conn.close()
except Exception as e:
    print(f"Error de conexión: {e}")
