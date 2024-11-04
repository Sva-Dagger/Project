from tkinter import *
import sqlite3

THEME_COLOR = "#375362"


class INVENTORY:
    def __init__(self):
        self.connection = sqlite3.connect("inventory.db")  # Connect to SQLite database
        self.cursor = self.connection.cursor()
        self.create_table()  # Create table if not exists
        self.window = Tk()
        self.INVENTORY_L()
        self.window.mainloop()

    # Create inventory table
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                brand TEXT NOT NULL,
                                name TEXT NOT NULL,
                                category TEXT,
                                stock INTEGER NOT NULL,
                                price REAL NOT NULL,
                                sale_price REAL NOT NULL
                            );''')
        self.connection.commit()

    def INVENTORY_L(self):
        self.DESTROY_WIDGET()
        self.window.configure(padx=100, pady=100, bg=THEME_COLOR)
        self.window.title("INVENTORY MANAGEMENT")
        self.window.configure(padx=50, bg=THEME_COLOR)
        self.window.geometry("1360x1200")
        self.NAME_label = Label(text="PRODUCT DETAILS", bg=THEME_COLOR, fg="black", font=("Ariel", 24, "bold"))
        self.NAME_label.grid(column=3, row=0, padx=20, pady=20)

        # Labels and Entries for product details
        self.ID_label = Label(text="PRODUCT ID:", bg=THEME_COLOR, fg="black", font=("Ariel", 10, "bold"))
        self.ID_label.grid(column=0, row=1, padx=10, pady=20)
        self.ID_entry = Entry(fg="black", bg=THEME_COLOR, width=10, font=("Ariel", 15))
        self.ID_entry.grid(column=1, row=1, padx=20, pady=20)

        self.BRAND_label = Label(text="PRODUCT BRAND:", bg=THEME_COLOR, fg="black", font=("Ariel", 10, "bold"))
        self.BRAND_label.grid(column=2, row=1, padx=20, pady=20)
        self.BRAND_entry = Entry(fg="black", bg=THEME_COLOR, width=10, font=("Ariel", 15))
        self.BRAND_entry.grid(column=3, row=1, padx=10, pady=20)

        self.STOCK_label = Label(text="PRODUCT STOCK:", bg=THEME_COLOR, fg="black", font=("Ariel", 10, "bold"))
        self.STOCK_label.grid(column=4, row=1, padx=20, pady=20)
        self.STOCK_entry = Entry(fg="black", bg=THEME_COLOR, width=10, font=("Ariel", 15))
        self.STOCK_entry.grid(column=5, row=1, padx=20, pady=20)

        self.CATEGORY_label = Label(text="PRODUCT CATEGORY:", bg=THEME_COLOR, fg="black", font=("Ariel", 10, "bold"))
        self.CATEGORY_label.grid(column=0, row=2, padx=20, pady=20)
        self.CATEGORY_entry = Entry(fg="black", bg=THEME_COLOR, width=10, font=("Ariel", 15))
        self.CATEGORY_entry.grid(column=1, row=2, padx=20, pady=20)

        self.NAME_label = Label(text="PRODUCT NAME:", bg=THEME_COLOR, fg="black", font=("Ariel", 10, "bold"))
        self.NAME_label.grid(column=2, row=2, padx=20, pady=20)
        self.NAME_entry = Entry(fg="black", bg=THEME_COLOR, width=10, font=("Ariel", 15))
        self.NAME_entry.grid(column=3, row=2, padx=20, pady=20)

        self.PRICE_label = Label(text="PRODUCT PRICE:", bg=THEME_COLOR, fg="black", font=("Ariel", 10, "bold"))
        self.PRICE_label.grid(column=4, row=2, padx=20, pady=20)
        self.PRICE_entry = Entry(fg="black", bg=THEME_COLOR, width=10, font=("Ariel", 15))
        self.PRICE_entry.grid(column=5, row=2, padx=20, pady=20)

        self.S_PRICE_label = Label(text="SALE PRICE:", bg=THEME_COLOR, fg="black", font=("Ariel", 10, "bold"))
        self.S_PRICE_label.grid(column=2, row=3, padx=20, pady=20)
        self.S_PRICE_entry = Entry(fg="black", bg=THEME_COLOR, width=10, font=("Ariel", 15))
        self.S_PRICE_entry.grid(column=3, row=3, padx=20, pady=20)

        # Buttons for actions
        self.ADD_BUTTON = Button(text="ADD ITEM", bg=THEME_COLOR, width=15, font=("Ariel", 10, "bold"),
                                 command=self.add_item)
        self.ADD_BUTTON.grid(column=0, row=4, padx=20, pady=20, columnspan=2)

        self.REMOVE_BUTTON = Button(text="REMOVE ITEM", bg=THEME_COLOR, width=15, font=("Ariel", 10, "bold"),
                                    command=self.delete_item)
        self.REMOVE_BUTTON.grid(column=1, row=4, padx=20, pady=20, columnspan=2)

        self.UPDATE_BUTTON = Button(text="UPDATE ITEM", bg=THEME_COLOR, width=15, font=("Ariel", 10, "bold"),
                                    command=self.update_item)
        self.UPDATE_BUTTON.grid(column=2, row=4, padx=20, pady=20, columnspan=2)

        self.CLEAR_I_BUTTON = Button(text="CLEAR INPUT", bg=THEME_COLOR, width=15, font=("Ariel", 10, "bold"),
                                     command=self.REMOVE_ALL_ENTRY)
        self.CLEAR_I_BUTTON.grid(column=3, row=4, padx=20, pady=20, columnspan=3)

        self.EXPORT_BUTTON = Button(text="EXPORT TO EXCEL", bg=THEME_COLOR, width=15, font=("Ariel", 10, "bold"),
                                    command=self.view_inventory)
        self.EXPORT_BUTTON.grid(column=4, row=4, padx=20, pady=20, columnspan=2)

    # Get input from entries
    def get_input(self):
        if (len(self.ID_entry.get()) > 0 and len(self.BRAND_entry.get()) > 0 and len(self.STOCK_entry.get()) > 0
                and len(self.CATEGORY_entry.get()) > 0 and len(self.NAME_entry.get()) > 0
                and len(self.PRICE_entry.get()) > 0 and len(self.S_PRICE_entry.get()) > 0):
            self.Item_name = self.ID_entry.get()
            self.BRAND = self.BRAND_entry.get()
            self.Quantity = int(self.STOCK_entry.get())
            self.CATEGORY = self.CATEGORY_entry.get()
            self.PRO_NAME = self.NAME_entry.get()
            self.PRICE = float(self.PRICE_entry.get())
            self.S_PRICE = float(self.S_PRICE_entry.get())
        else:
            self.SHOW_MESSAGE("Please input something")

    # Remove entry inputs
    def REMOVE_ALL_ENTRY(self):
        self.ID_entry.delete(0, END)
        self.BRAND_entry.delete(0, END)
        self.STOCK_entry.delete(0, END)
        self.CATEGORY_entry.delete(0, END)
        self.NAME_entry.delete(0, END)
        self.PRICE_entry.delete(0, END)
        self.S_PRICE_entry.delete(0, END)

    # Add item to the database
    def add_item(self):
        self.get_input()
        self.REMOVE_ALL_ENTRY()
        self.cursor.execute('''INSERT INTO inventory (brand, name, category, stock, price, sale_price)
                               VALUES (?, ?, ?, ?, ?, ?)''',
                            (self.BRAND, self.PRO_NAME, self.CATEGORY, self.Quantity, self.PRICE, self.S_PRICE))
        self.connection.commit()
        self.SHOW_MESSAGE(f"Item {self.PRO_NAME} added successfully")

    # View inventory items
    def view_inventory(self):
        self.cursor.execute("SELECT * FROM inventory")
        items = self.cursor.fetchall()
        if not items:
            self.SHOW_MESSAGE("Inventory is empty")
        else:
            inventory_text = "\n".join(
                [f"ID: {item[0]}, Brand: {item[1]}, Name: {item[2]}, Stock: {item[4]}" for item in items])
            self.SHOW_MESSAGE(inventory_text)

    # Update item in the database
    def update_item(self):
        self.get_input()
        self.cursor.execute('''UPDATE inventory SET stock=?, price=?, sale_price=? WHERE name=?''',
                            (self.Quantity, self.PRICE, self.S_PRICE, self.PRO_NAME))
        self.connection.commit()
        self.SHOW_MESSAGE(f"Item {self.PRO_NAME} updated successfully")

    # Delete item from the database
    def delete_item(self):
        self.get_input()
        self.cursor.execute("DELETE FROM inventory WHERE name=?", (self.PRO_NAME,))
        self.connection.commit()
        self.SHOW_MESSAGE(f"Item {self.PRO_NAME} deleted successfully")

    # Destroy widgets
    def DESTROY_WIDGET(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def SHOW_MESSAGE(self, message: str):
        self.DESTROY_WIDGET()
        self.window.configure(padx=400, pady=200, bg=THEME_COLOR)
        message_label = Label(text=message, width=25, bg=THEME_COLOR, fg="white", font=("Ariel", 28, "bold"))
        message_label.grid(pady=50)

        back_button = Button(text="Back", bg=THEME_COLOR, fg="black", font=("Ariel", 24), command=self.INVENTORY_L)
        back_button.grid(pady=10)


INVENTORY()