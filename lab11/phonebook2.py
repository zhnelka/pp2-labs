import psycopg2

try:
    connection = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="12345", 
        host="127.0.0.1", 
        port="5432"
    )

    cursor = connection.cursor()
    connection.autocommit = True
    cursor.execute("SELECT version();")   
    print(f"Server version: {cursor.fetchone()}")

    cursor.execute(''' CREATE OR REPLACE FUNCTION get_pagination_data(
                        _limit INT,
                        _offset INT)
                    RETURNS TABLE(
                        name TEXT,
                        phonenumber TEXT
                    )
                    LANGUAGE plpgsql
                    AS $$
                    BEGIN
                        RETURN QUERY SELECT *
                        FROM phonebook
                        LIMIT _limit
                        OFFSET _offset;
                    END;
                    $$''')

    cursor.execute(""" CREATE OR REPLACE PROCEDURE add_update_user(
                        _name TEXT,
                        _phone TEXT)
                LANGUAGE plpgsql
                AS $$
                BEGIN
                    UPDATE phonebook SET phonenumber = _phone WHERE name = _name;
                    IF NOT FOUND THEN
                        INSERT INTO phonebook (name, phonenumber) VALUES (_name, _phone);
                    END IF;
                END
                $$
                """)

    cursor.execute(""" CREATE OR REPLACE PROCEDURE delete_user(
                    _n TEXT,
                    _m TEXT)
                    LANGUAGE plpgsql
                    AS $$
                    BEGIN
                        IF _m = 'p' THEN
                            DELETE FROM phonebook WHERE phone = _n;
                        ELSE
                            DELETE FROM phonebook WHERE name = _n;
                        END IF;
                    END
                    $$""")

    # Вывод данных

    pattern = input()
    cursor.execute("SELECT * FROM phonebook WHERE CONCAT(name, phonenumber) LIKE '%"+pattern+"%'")
    result = cursor.fetchall()
    for i in result:
        print(i)
                
    # Процедура для записи в таблицу
    
    user = input()
    phone = input()
    cursor.execute("CALL add_update_user(%s, %s)",(user, phone))
            
    # Процедура для записи нескольких контактов сразу

    values = input()
    values = values.split(" ")
    i = 0
    while i != len(values):
        n, p = values[i], values[i + 1]
        try:
            if type(int(p)) is int:
                cursor.execute("CALL add_update_user(%s, %s)", (n, p))
        except:
            pass
        i += 2

    # Процедура для фильтра

    
    lim = input()
    off = input()
            
    cursor.execute('SELECT * FROM get_pagination_data(%s, %s)',(lim, off))
    result = cursor.fetchall()
    for i in result:
        print(i)

    # Удаление
                
    delete = input()
    name_phone = input()
    cursor.execute("CALL delete_user(%s, %s)",(name_phone, delete))
        
except Exception as error:
    print("error:", error)

finally:
    if connection:
        connection.close()
        print("connection closed")