import sqlite3

class ContactManager:
    def __init__(self, db_name='contacts.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                          (id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL,
                           phone TEXT NOT NULL,
                           email TEXT NOT NULL)''')
        self.conn.commit()

    def add_contact(self, name, phone, email):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
                       (name, phone, email))
        self.conn.commit()

    def get_contacts(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        return cursor.fetchall()

    def update_contact(self, contact_id, name, phone, email):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",
                       (name, phone, email, contact_id))
        self.conn.commit()

    def delete_contact(self, contact_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        self.conn.commit()
