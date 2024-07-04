import tkinter as tk
from tkinter import ttk, messagebox
from contact_manager import ContactManager

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("600x400")
        
        self.manager = ContactManager()
        
        self.create_widgets()
        self.load_contacts()

    def create_widgets(self):
        # Create input frame
        input_frame = tk.Frame(self.root, padx=10, pady=10)
        input_frame.pack(fill=tk.X)

        # Name
        tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Phone
        tk.Label(input_frame, text="Phone:").grid(row=1, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(input_frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        # Email
        tk.Label(input_frame, text="Email:").grid(row=2, column=0, sticky=tk.W)
        self.email_entry = tk.Entry(input_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        button_frame = tk.Frame(self.root, padx=10, pady=10)
        button_frame.pack(fill=tk.X)
        
        self.add_button = tk.Button(button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.update_button = tk.Button(button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = tk.Button(button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(button_frame, text="Clear Fields", command=self.clear_fields)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Contact list
        self.contact_tree = ttk.Treeview(self.root, columns=("ID", "Name", "Phone", "Email"), show='headings')
        self.contact_tree.heading("ID", text="ID")
        self.contact_tree.heading("Name", text="Name")
        self.contact_tree.heading("Phone", text="Phone")
        self.contact_tree.heading("Email", text="Email")

        self.contact_tree.column("ID", width=30)
        self.contact_tree.column("Name", width=150)
        self.contact_tree.column("Phone", width=150)
        self.contact_tree.column("Email", width=200)

        self.contact_tree.bind("<<TreeviewSelect>>", self.on_select)
        
        self.contact_tree.pack(fill=tk.BOTH, expand=True)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            self.manager.add_contact(name, phone, email)
            messagebox.showinfo("Success", "Contact added successfully")
            self.clear_fields()
            self.load_contacts()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def load_contacts(self):
        for item in self.contact_tree.get_children():
            self.contact_tree.delete(item)
        
        contacts = self.manager.get_contacts()
        for contact in contacts:
            self.contact_tree.insert('', tk.END, values=contact)

    def on_select(self, event):
        selected_item = self.contact_tree.selection()[0]
        contact = self.contact_tree.item(selected_item, 'values')

        self.clear_fields()
        
        self.contact_id = contact[0]
        self.name_entry.insert(0, contact[1])
        self.phone_entry.insert(0, contact[2])
        self.email_entry.insert(0, contact[3])

    def update_contact(self):
        if hasattr(self, 'contact_id'):
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()

            if name and phone and email:
                self.manager.update_contact(self.contact_id, name, phone, email)
                messagebox.showinfo("Success", "Contact updated successfully")
                self.clear_fields()
                self.load_contacts()
            else:
                messagebox.showwarning("Input Error", "Please fill in all fields")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update")

    def delete_contact(self):
        if hasattr(self, 'contact_id'):
            self.manager.delete_contact(self.contact_id)
            messagebox.showinfo("Success", "Contact deleted successfully")
            self.clear_fields()
            self.load_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        if hasattr(self, 'contact_id'):
            del self.contact_id

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
