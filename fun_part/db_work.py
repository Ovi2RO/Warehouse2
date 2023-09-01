import sqlite3

class Db:
    def __init__(self):
        self.conn = sqlite3.connect("/home/dci-student/Desktop/Ola/Database/08-23-Database/Data08.31/Warehouse2/Warehouse2/db/products.db")
        self.cursor = self.conn.cursor()

    def add_entry(self, table_name, values):
        # self.table_name = table_name
        # self.values = values
        self.cursor.execute(f"INSERT INTO {table_name} VALUES {values}")
        self.conn.commit() 
        self.view_entries()     
            
    def delete_entry(self, table_name, condition):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.conn.commit()
        self.view_entries() 
    
    def modify_entry(self, table_name, set_values, condition):
        self.cursor.execute(f"UPDATE {table_name} SET {set_values} WHERE {condition}")
        self.conn.commit()
        self.view_entries()
    
    def view_entries(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        entries = self.cursor.fetchall()
        return entries
    
    
    
db = Db() 
for row in db.view_entries("products"):
    print(row)