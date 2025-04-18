import psycopg2

try:
    connection = psycopg2.connect(
        database="postgres", 
        user="mrtva_zhanel", 
        password="12345", 
        host="127.0.0.1", 
        port="5432"
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")   
        print(f"Server version: {cursor.fetchone()}")

    # Проверяем наличие таблицы
    aa = input("Is the table created? (yes/no) ")
    if aa == "no":
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE phonebook(
                    name VARCHAR NOT NULL,
                    phonenumber VARCHAR NOT NULL PRIMARY KEY);"""
            )
            print("Table created successfully.")
    elif aa == 'yes':
        dd = input("Add something? (yes/no) ")
        if dd == "yes":
            # Добавление данных в таблицу из консоли
            x = input("Enter name: ")
            y = input("Enter phone number: ")
            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO phonebook (name, phonenumber)
                       VALUES (%s, %s);""", (x, y)
                )
                print("Record added successfully.")
            
        elif dd == "no":
            bb = input('Search something? (yes/no) ')
            if bb == "yes":
                # Поиск данных
                choice = input("Search by name or phone number? (name/phonenumber): ")
                if choice == "phonenumber":
                    x = input("Enter phone number: ")
                    with connection.cursor() as cursor:
                        cursor.execute(
                            """SELECT * FROM phonebook WHERE phonenumber = %s;""", (x,)
                        )
                        result = cursor.fetchone()
                        print(result if result else "No records found.")
                elif choice == "name":
                    x = input("Enter name: ")
                    with connection.cursor() as cursor:
                        cursor.execute(
                            """SELECT * FROM phonebook WHERE name = %s;""", (x,)
                        )
                        result = cursor.fetchone()
                        print(result if result else "No records found.")
            elif bb == "no":
                cc = input("Drop something? (yes/no) ")
                if cc == "yes":
                    drop = input("Enter name or phone number to delete: ")
                    with connection.cursor() as cursor:
                        cursor.execute(
                            """DELETE FROM phonebook WHERE name = %s OR phonenumber = %s;""", 
                            (drop, drop)
                        )
                        print("Record deleted successfully.")
                
except Exception as error:
    print(f"Error: {error}")

finally:
    if connection:
        connection.close()
        print("Connection closed.")
