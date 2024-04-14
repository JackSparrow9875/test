import os

def delete_database(db_name):
    if os.path.exists(db_name):
        os.remove(db_name)
        print(f"The database {db_name} has been deleted successfully.")
    else:
        print("The database does not exist.")

delete_database('Library.db')
