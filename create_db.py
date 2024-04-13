import sqlite3

def database_creation():
    conn = None
    try:
        conn = sqlite3.connect('Library')
        print('Database has been created successfully.')
        create_users_table(conn) 
        create_sections_table(conn) 
        create_books_table(conn) 
    except Exception as e:
        print(f'An error occured: {str(e)}')
    finally:
        if conn:
            conn.close()


def create_users_table(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE Users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL,
            Password TEXT NOT NULL
        )
    ''')
    print('Users table has been created successfully')
    conn.commit()

def create_sections_table(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE Sections (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            DateCreated TEXT NOT NULL,
            Description TEXT
        )
    ''')
    print('Sections table has been created successfully')
    conn.commit()

def create_books_table(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE Books (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Content TEXT NOT NULL,
            Authors TEXT NOT NULL,
            DateIssued TEXT NOT NULL,
            ReturnDate TEXT
        )
    ''')
    print('Books table has been created successfully')
    conn.commit()


if __name__ == '__main__':
    database_creation()
