import psycopg2

try:

    connection = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="12345", 
        host="127.0.0.1", 
        port="5432"
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")   

        print(f"Server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE snake(
                user_name varchar NOT NULL PRIMARY KEY,
                user_score INTEGER NOT NULL );"""
        )

except Exception as error:
    print("error:", error)

finally:
    if connection:
        connection.close()
        print("connection closed")