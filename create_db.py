import sqlite3

def database_creation():
    conn = None
    try:
        conn = sqlite3.connect('Library')
        print('Database has been created successfully.')
    except Exception as e:
        print(f'An error occured: {str(e)}')
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    database_creation()


