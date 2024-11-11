THEME_COLOR ="#375362"
from SQL import *
from tkinter import *
import sqlite3
import datetime
import string
import random
window= Tk()
SQL=SQL()
from TOOLS import vaidator
TIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class UI:
    def __init__(self):
        self.Validator = vaidator()
        window.configure(padx=180, pady=50, bg=THEME_COLOR)
        window.geometry("1600x1200")
        self.connection = sqlite3.connect("Account.db")
        self.cursor = self.connection.cursor()

        self.buttons = [
            ("1", 0, 2), ("2", 1, 2), ("3", 2, 2),
            ("4", 0, 3), ("5", 1, 3), ("6", 2, 3),
            ("7", 0, 4), ("8", 1, 4), ("9", 2, 4),
            ("0", 1, 5)
        ]

    def password_generator(self):
        letters = string.ascii_letters  # Includes both lowercase and uppercase letters
        numbers = string.digits
        symbols = "!#$%&()*+"

        nr_letters = 4
        nr_symbols = 2
        nr_numbers = 3

        # Generate password parts
        password = (
                ''.join(random.choice(letters) for _ in range(nr_letters)) +
                ''.join(random.choice(symbols) for _ in range(nr_symbols)) +
                ''.join(random.choice(numbers) for _ in range(nr_numbers))
        )

        # Shuffle the password to randomize character positions
        password = ''.join(random.sample(password, len(password)))

        # Insert password into entry field
        self.PG_button = Button(text="Pass Gen", fg="black",
                                bg=THEME_COLOR, font=("Ariel", 10, "bold"),
                                command=lambda t=password: self.password_entry.insert(END, t))
        self.PG_button.grid(column=2, row=3, padx=20, pady=20)


        # Create a button to show or hide the password

    def show_password(self):
        self.password_entry = Entry(width=13, font=("Ariel", 20))
        self.password_entry.grid(column=1, row=3, pady=20)



    def Login_UI(self):
        self.DESTROY_WIDGET()
        window.configure(padx=250, pady=50, bg=THEME_COLOR)
        window.geometry("1600x1200")
        self.Welcome_label = Label(text="WELCOME TO OUR ATM MACHINE",
                                   width=30, bg=THEME_COLOR, fg="white",
                                   font=("Ariel", 20, "bold"))
        self.Welcome_label.grid(column=1, row=0, pady=20)

        self.Insert_label = Label(text="Please Enter Your Account Details",
                                  width=30, bg=THEME_COLOR, fg="white",
                                  font=("Ariel", 20, "bold"))
        self.Insert_label.grid(column=1, row=1, pady=20)

        self.email_entry = Entry(width=13, font=("Ariel", 20))
        self.email_entry.grid(column=1, row=2, pady=20)

        self.email_label = Label(text="Email:", bg=THEME_COLOR, fg="white", font=("Ariel", 20))
        self.email_label.grid(column=0, row=2, pady=20)

        self.password_entry = Entry(width=13,show="*", font=("Ariel", 20))
        self.password_entry.grid(column=1, row=3, pady=20)

        self.password_label = Label(text="password:", bg=THEME_COLOR, fg="white", font=("Ariel", 20))
        self.password_label.grid(column=0, row=3, pady=20)

        self.password_generator()

        self.Log = Button(text="Log In",
                                  width=10, bg=THEME_COLOR, fg="black",
                                  font=("Ariel", 20, "bold"), command=self.Check_Login)
        self.Log.grid(column=0, row=4, pady=20)

        self.Register = Button(text="Register",
                                  width=10, bg=THEME_COLOR, fg="black",
                                  font=("Ariel", 20, "bold"), command=self.Register_Account_widget)
        self.Register.grid(column=2, row=4, pady=20)
        window.mainloop()

    def Check_Login(self):
        self.email = self.email_entry.get().lower()
        self.password = self.password_entry.get()
        password = self.password
        if self.Validator.is_valid_email(self.email) and self.Validator.is_valid_password(password):
            # Check if the account exists with the provided credentials
            self.cursor.execute("SELECT Account_no FROM Account WHERE Email=? AND Password=?", (self.email, self.password))
            list_1 = self.cursor.fetchall()
            if len(list_1) == 1:  # Exactly one match found
                self.MENU_OPTION()  # Log in the user
            elif len(list_1) > 1:  # More than one match found
                self.SHOW_MESSAGE("Multiple accounts found with the same credentials. Please contact support.")
            else:  # No match found
                self.SHOW_MESSAGE("You entered wrong credentials.")
        else:
            self.SHOW_MESSAGE("Please enter correct email/password format")

    def Register_Account_widget(self):
        self.DESTROY_WIDGET()
        window.configure(padx=250, pady=50, bg=THEME_COLOR)
        window.geometry("1600x1200")
        self.Welcome_label = Label(text="WELCOME TO OUR ATM MACHINE",
                                   width=30, bg=THEME_COLOR, fg="white",
                                   font=("Ariel", 20, "bold"))
        self.Welcome_label.grid(column=1, row=0, pady=20)

        self.Insert_label = Label(text="Please Enter Your Account Details",
                                  width=30, bg=THEME_COLOR, fg="white",
                                  font=("Ariel", 20, "bold"))
        self.Insert_label.grid(column=1, row=1, pady=20)

        self.account_entry = Entry(width=13, font=("Ariel", 15))
        self.account_entry.grid(column=1, row=2, pady=20)

        self.account_label = Label(text="Name:", bg=THEME_COLOR, fg="white", font=("Ariel", 20))
        self.account_label.grid(column=0, row=2, pady=20)

        self.Initial_entry = Entry(width=5, font=("Ariel", 15))
        self.Initial_entry.grid(column=2, row=2, pady=20)

        self.email_entry = Entry(width=13, font=("Ariel", 15))
        self.email_entry.grid(column=1, row=3, pady=20)

        self.email_label = Label(text="Email:", bg=THEME_COLOR, fg="white", font=("Ariel", 20))
        self.email_label.grid(column=0, row=3, pady=20)

        self.password_entry = Entry(width=13, font=("Ariel", 15))
        self.password_entry.grid(column=1, row=4, pady=20)

        self.password_label = Label(text="password:", bg=THEME_COLOR, fg="white", font=("Ariel", 20))
        self.password_label.grid(column=0, row=4, pady=20)

        self.confirm_password_entry = Entry(width=13, font=("Ariel", 15))
        self.confirm_password_entry.grid(column=1, row=5, pady=20)

        self.confirm_password_label = Label(text="confirm_password:", bg=THEME_COLOR, fg="white", font=("Ariel", 20))
        self.confirm_password_label.grid(column=0, row=5, pady=20)

        self.password_generator()

        self.Register_button = Button(text="Register",
                                      width=10, bg=THEME_COLOR, fg="black",
                                      font=("Ariel", 15, "bold"), command=self.Register_Account)
        self.Register_button.grid(column=0, row=6, pady=20)

        self.exit_button = Button(text="EXIT", width=10,
                                  bg=THEME_COLOR, fg="black",
                                  font=("Ariel", 15, "bold"), command=self.Login_UI)
        self.exit_button.grid(column=2, row=6, pady=10)

    def Register_Account(self):
        Name = self.account_entry.get().title()
        Email = self.email_entry.get().lower()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if self.Validator.is_valid_email(Email) and self.Validator.is_valid_password(password):
            if password == confirm_password:
                # Fetch all existing emails from the Account table
                self.cursor.execute("SELECT Email FROM Account")
                existing_emails = [email[0] for email in self.cursor.fetchall()]

                # Check if the email already exists
                if Email in existing_emails:
                    self.SHOW_MESSAGE(f"Your email {Email} already exists.")
                else:
                    # If the email is new, proceed with the registration
                    SQL.initialize(Name)
                    SQL.create_account(Name, password, Email)
                    self.SHOW_MESSAGE(f"Your email ID {Email} has been successfully registered.")
            else:
                # If passwords do not match
                self.SHOW_MESSAGE("Confirm Password does not match.")
        else:
            self.SHOW_MESSAGE("Please enter correct email/password format")

    def MENU_OPTION(self):
        self.DESTROY_WIDGET()
        window.configure(padx=200, pady=150, bg=THEME_COLOR)
        window.geometry("4000x4000")
        self.ATM_LABEL = Label(text="YOUR_BANK",
                               bg=THEME_COLOR, fg="white",
                               font=("Ariel", 60, "bold"))
        self.ATM_LABEL.grid(column=1, row=0, pady=15)
        self.option_label = Label(text="MAIN MENU",
                                  bg=THEME_COLOR, fg="white",
                                  font=("Ariel", 24, "bold"))
        self.option_label.grid(column=1, row=1, pady=10)

        self.balance_button = Button(text="CHECK BALANCE",width=15,
                                     bg=THEME_COLOR, fg="black",
                                     font=("Ariel", 20, "bold"), command=lambda : self.PIN("BALANCE"))
        self.balance_button.grid(column=0, row=3, pady=10)

        self.deposit_button = Button(width=15, text="DEPOSIT",
                                     bg=THEME_COLOR, fg="black",
                                     font=("Arial", 20, "bold"), command=lambda : self.PIN("DEPOSIT"))
        self.deposit_button.grid(column=1, row=4, pady=10)

        self.withdraw_button = Button(text="WITHDRAW",width=10,
                                      bg=THEME_COLOR, fg="black",
                                      font=("Ariel", 20, "bold"), command=lambda : self.PIN("WITHDRAW"))
        self.withdraw_button.grid(column=2, row=3, pady=10)

        self.trans_history_button = Button(text="TRANS HISTORY", width=15,
                                           fg="black", bg=THEME_COLOR, font=("Ariel", 20, "bold"),
                                           command=lambda : self.PIN("TRANS_HISTORY"))
        self.trans_history_button.grid(column=0, row=4, pady=10)

        self.exit_button = Button(text="EXIT",width=10,
                                  bg=THEME_COLOR, fg="black",
                                  font=("Ariel", 20, "bold"), command=self.Login_UI)
        self.exit_button.grid(column=2, row=4, pady=10)

    def CREATE_NUMBER_BUTTON(self):
        for (text, col, row) in self.buttons:
            self.button = Button(text=text, fg="black",
                            bg=THEME_COLOR, font=("Ariel", 28, "bold"),
                            command=lambda t=text: self.pin_entry.insert(END, t))
            self.button.grid(column=col, row=row, padx=20, pady=20)

    def PIN(self,action):
        self.DESTROY_WIDGET()
        self.CREATE_NUMBER_BUTTON()
        window.geometry("4000x4000")
        window.configure(padx=250, pady=150, bg=THEME_COLOR)
        self.pin_entry_label = Label(text="PLEASE ENTER YOUR PIN",
                                     bg=THEME_COLOR, fg="white",
                                     font=("Ariel", 20, "bold"))
        self.pin_entry_label.grid(column=4, row=1, pady=20)

        # Create an Entry widget for the PIN
        self.pin_entry = Entry(width=13, show="*", font=("Ariel", 20))
        self.pin_entry.grid(column=4, row=2, pady=20)

        # Create buttons for actions
        self.cancel_button = Button(text="CANCEL", width=10,
                                    fg="black", bg=THEME_COLOR,
                                    font=("Ariel", 28, "bold"), command=self.Login_UI)
        self.cancel_button.grid(column=5, row=2, padx=20, pady=20, columnspan=2)

        self.clear_button = Button(text="CLEAR", width=10, fg="black", bg=THEME_COLOR, font=("Ariel", 28, "bold"),
                                   command=self.CLEAR_PIN)
        self.clear_button.grid(column=5, row=3, padx=20, pady=20, columnspan=2)
        self.ENTER_BUTTON()
        if action == "BALANCE":
            self.BALANCE_ENTER_BUTTON()
        elif action == "WITHDRAW":
            self.WITHDRAWAL_ENTER_BUTTON()
        elif action == "DEPOSIT":
            self.DEPOSIT_ENTER_BUTTON()
        elif action == "TRANS_HISTORY":
            self.TRANSACTION_ENTER_BUTTON()

    def PIN_ENTRY(self):
        self.PIN(action=str)
        self.ENTER_BUTTON()

    def ENTER_BUTTON(self):
        self.enter_button = Button(text="ENTER", width=10, fg="black", bg=THEME_COLOR, font=("Ariel", 28, "bold"),
                                       command=self.CHECK_PIN)
        self.enter_button.grid(column=5, row=4, padx=20, pady=20, columnspan=2)

    def DEPOSIT_ENTER_BUTTON(self):
        self.enter_button.configure(command=self.DEPOSIT_CHECK_PIN)

    def BALANCE_ENTER_BUTTON(self):
        self.enter_button.configure(command=self.BALANCE_CHECK_PIN)

    def WITHDRAWAL_ENTER_BUTTON(self):
        self.enter_button.configure(command=self.WITHDRAWAL_CHECK_PIN)

    def TRANSACTION_ENTER_BUTTON(self):
        self.enter_button.configure(command=self.TRANSACTION_CHECK_PIN)

    def CHECK_PIN(self):
        pin = self.pin_entry.get()
        if pin == "1234":  # Example PIN check
            self.MENU_OPTION()
            return True
        self.CLEAR_PIN()

    def BALANCE_CHECK_PIN(self):
        pin = self.pin_entry.get()
        if pin == "1234":  # Example PIN check
            self.show_balance()
            return True
        self.CLEAR_PIN()

    def show_balance(self):
        Email = self.email
        Password = self.password
        self.cursor.execute("SELECT Account_no From Account WHERE Email=? AND Password=?", (Email, Password))
        name = self.cursor.fetchone()
        self.cursor.execute("SELECT Balance from Account WHERE Account_no=?", (name))
        Balance = self.cursor.fetchone()
        self.SHOW_MESSAGE(f"your available Balance is {Balance[0]}$")

    def DEPOSIT(self):
        self.DESTROY_WIDGET()
        window.configure(padx=200, pady=100, bg=THEME_COLOR)
        window.geometry("4000x4000")
        self.title_label = Label(text="DEPOSIT YOUR AMOUNT", width=15,
                                 bg=THEME_COLOR, fg="white",
                                 font=("Arial", 20, "bold"))
        self.title_label.grid(column=4, row=0, pady=10)

        self.title_label = Label(text="Deposit Amount: ",
                                 bg=THEME_COLOR, fg="white",
                                 font=("Arial", 20))
        self.title_label.grid(column=3, row=1, pady=10)
        self.deposit_amount_entry = Entry(width=10, font=("Arial", 30))
        self.deposit_amount_entry.grid(column=4, row=1, padx=20, pady=20)
        for (text, col, row) in self.buttons:
            button = Button(text=text, fg="black",
                            bg=THEME_COLOR, font=("Ariel", 24, "bold"),
                            command=lambda t=text: self.deposit_amount_entry.insert(END, t))
            button.grid(column=col, row=row, padx=20, pady=20)

        self.Deposit_button = Button(text="DEPOSIT", width=10,
                                     bg=THEME_COLOR,
                                     fg="black", font=("Ariel", 20), command=self.process_deposit)
        self.Deposit_button.grid(column=5, row=2, padx=20, pady=20)

        self.clear_button = Button(text="CLEAR", width=10, fg="black", bg=THEME_COLOR, font=("Ariel", 20))
        self.clear_button.grid(column=5, row=3, padx=20, pady=20)

        back_button = Button(text="BACK", width=10, bg=THEME_COLOR, fg="black",
                             font=("Ariel", 20), command=self.Login_UI)
        back_button.grid(column=5, row=4, pady=20, padx=20)

    def process_deposit(self):
        Email = self.email
        amount=float(self.deposit_amount_entry.get())
        if amount%100 == 0:
            SQL.record_deposit(Email, amount)
            # Retrieve the updated balance
            self.cursor.execute('''
                        SELECT Balance
                        FROM Account
                        WHERE Email = ?
                    ''', (Email,))
            Balance = self.cursor.fetchone()[0]
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Write transaction to file
            with open(f"{Email}.txt", "a") as file:
                file.write(f"{timestamp} | Deposit amount {amount} | Your Balance {Balance}\n")

            self.SHOW_MESSAGE(f"Your Amount: Rs. {amount} has been deposited successfully.\n Your balance is Rs.{Balance}")
        else:
            self.SHOW_MESSAGE(f"Available denomination for deposit is 100$, 200$, 500$")




    def WITHDRAW(self):

        self.DESTROY_WIDGET()
        self.CREATE_NUMBER_BUTTON()
        window.configure(padx=150, pady=100, bg=THEME_COLOR)
        window.geometry("4000x4000")
        # Clear existing widgets
        self.Withdrawal_entry = Entry(width=15, font=("Ariel", 30))
        self.Withdrawal_entry.grid(column=4, row=2, pady=20, padx=20)

        for (text, col, row) in self.buttons:
            button = Button(text=text, fg="black",
                            bg=THEME_COLOR, font=("Ariel", 28, "bold"),
                            command=lambda t=text: self.Withdrawal_entry.insert(END, t))
            button.grid(column=col, row=row, padx=20, pady=20)

        self.pin_label = Label(text="ENTER AVAILABLE AMOUNT TO WITHDRAW\n$100\n$200\n$500", width=28, bg=THEME_COLOR,
                               fg="white", font=("Ariel", 14, "bold"))
        self.pin_label.grid(column=4, row=0, pady=20, padx=20)

        self.confirm_button = Button(text="CONFIRM", width=10,
                                     command=self.process_withdrawal, bg=THEME_COLOR,
                                     fg="black", font=("Ariel", 24, "bold"))
        self.confirm_button.grid(column=5, row=2, padx=20, pady=10)

        self.clear_button = Button(text="CLEAR", width=10, fg="black",
                                   bg=THEME_COLOR, font=("Ariel", 24, "bold")
                                   ,command=self.CLEAR_WITHDRAWAL_ENTRY)
        self.clear_button.grid(column=5, row=3, padx=20, pady=10)

        self.back_button = Button(text="BACK", width=10, bg=THEME_COLOR, fg="black",
                                  font=("Ariel", 24, "bold"), command=self.Login_UI)
        self.back_button.grid(column=5, row=4, pady=20, padx=20)

    def process_withdrawal(self):
        Email = self.email
        amount = float(self.Withdrawal_entry.get())
        self.cursor.execute('SELECT Balance FROM Account WHERE Email = ?', (Email,))
        current_balance = self.cursor.fetchone()[0]
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if current_balance >= amount:
            SQL.record_withdrawal(Email, amount)
            self.cursor.execute('''
                                                    SELECT Balance
                                                    FROM Account
                                                    WHERE Email = ?
                                                ''', (Email,))
            Balance = self.cursor.fetchone()[0]
            self.SHOW_MESSAGE(f"Your Amount: ${amount} has been withdrawn successfully.\n Your balance is Rs.{Balance}")
            with open(f"{Email}.txt", "a") as file:
                file.write(f"{timestamp} | Withdrawn amount ${amount} | Your Balance ${Balance}\n")
        else:
            self.SHOW_MESSAGE(f"Your Amount: ${amount} has not been credited.\n due to insufficient balance.")


    def VIEW_TRANSACTION(self):
        self.DESTROY_WIDGET()
        window.configure(padx=150, pady=50, bg=THEME_COLOR)
        window.geometry("4000x4000")
        transaction_text = Text(height=30, width=50)
        transaction_text.grid(padx=300, pady=10)

        try:
            with open(f"{self.email}.txt", "r") as file:
                transactions = file.readlines()
                for transaction in transactions:
                    transaction_text.insert(END, transaction)  # Insert each transaction into the Text widget
        except FileNotFoundError:
            transaction_text.insert(END, "No transaction history found.")

        close_button = Button(text="Close", command=self.Login_UI)
        close_button.grid(pady=5)


    def DEPOSIT_CHECK_PIN(self):
        pin = self.pin_entry.get()
        if pin == "1234":  # Example PIN check
            self.DEPOSIT()
            return True
        self.CLEAR_PIN()

    def WITHDRAWAL_CHECK_PIN(self):
        pin = self.pin_entry.get()
        if pin == "1234":  # Example PIN check
            self.WITHDRAW()
            return True
        self.CLEAR_PIN()

    def TRANSACTION_CHECK_PIN(self):
        pin = self.pin_entry.get()
        if pin == "1234":  # Example PIN check
            self.VIEW_TRANSACTION()
            return True
        self.CLEAR_PIN()

    def CLEAR_PIN(self):
        self.pin_entry.delete(0, END)

    def DESTROY_WIDGET(self):
        for widget in window.winfo_children():
            widget.destroy()

    def SHOW_MESSAGE(self, message:str):
        # Clear existing widgets
        self.DESTROY_WIDGET()
        message_label = Label(text=message, width=100, bg=THEME_COLOR, fg="white", font=("Ariel", 20, "bold"))
        message_label.pack(pady=20)

        back_button = Button(text="Back", bg=THEME_COLOR, fg="black", font=("Ariel", 24), command=self.Login_UI)
        back_button.pack(pady=10)

    def CLEAR_WITHDRAWAL_ENTRY(self):
        self.Withdrawal_entry.delete(0, END)

    def CLEAR_DEPOSIT_ENTRY(self):
        self.deposit_amount_entry.delete(0, END)