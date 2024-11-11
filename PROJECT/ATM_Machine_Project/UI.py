
from tkinter import *
THEME_COLOR ="#375362"
import datetime
import json
import smtplib


class UI:
    def __init__(self):
        self.balance = None
        self.messagebox = None
        self.Deposit_button = None
        self.amount: int
        self.TIME_NOW: str
        self.Withdrawal_entry = None
        self.BALANCE_PIN: int
        self.WITHDRAW_PIN: int
        self.DEPOSIT_PIN:int
        self.TRANSACTION_PIN: int
        self.action:str
        self.my_email = "hackersiva847@gmail.com"
        self.password = "ccnffohqpwivwijz"
        self.back_button = None
        self.buttons = [
            ("1", 0, 2), ("2", 1, 2), ("3", 2, 2),
            ("4", 0, 3), ("5", 1, 3), ("6", 2, 3),
            ("7", 0, 4), ("8", 1, 4), ("9", 2, 4),
            ("0", 1, 5)
        ]

        self.process_withdrawal = None
        self.window = Tk()
        self.pin_label = None
        self.confirm_button = None
        self.deposit_amount_entry = None
        self.title_label = None
        self.transactions = None
        self.enter_button = None
        self.button = None
        self.clear_button = None
        self.cancel_button = None

        self.pin_entry_label = None
        self.pin_entry = None

        self.exit_button = None
        self.withdraw_button = None
        self.trans_history_button = None
        self.option_label = None
        self.deposit_button = None
        self.balance_button = None
        self.ATM_LABEL = None
        self.Card_button = None
        self.Insert_label = None
        self.Welcome_label = None
    def WELCOME(self):
        self.DESTROY_WIDGET()
        self.window.configure(padx=350, pady=200, bg=THEME_COLOR)
        self.window.geometry("1600x1200")
        self.Welcome_label = Label(text="WELCOME TO OUR ATM MACHINE",
                                   width=30, bg=THEME_COLOR, fg="white",
                                   font=("Ariel", 20, "bold"))
        self.Welcome_label.grid(column=1, row=0, pady=20)

        self.Insert_label = Label(text="PLEASE INSERT YOUR CARD",
                                  width=30, bg=THEME_COLOR, fg="white",
                                  font=("Ariel", 20, "bold"))
        self.Insert_label.grid(column=1, row=1, pady=20)

        self.Card_button = Button(text="INSERT CARD",
                                  width=30, bg=THEME_COLOR, fg="black",
                                  font=("Ariel", 28, "bold"), command=self.PIN_ENTRY)
        self.Card_button.grid(column=1, row=2, pady=20)
        self.window.mainloop()

    def PIN(self,action):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.CREATE_NUMBER_BUTTON()
        self.window.geometry("4000x4000")
        self.window.configure(padx=250, pady=150, bg=THEME_COLOR)
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
                                    font=("Ariel", 28, "bold"))
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
            self.SHOW_BALANCE()
            return True
        self.CLEAR_PIN()

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

    def CREATE_NUMBER_BUTTON(self):
        for (text, col, row) in self.buttons:
            self.button = Button(text=text, fg="black",
                            bg=THEME_COLOR, font=("Ariel", 28, "bold"),
                            command=lambda t=text: self.pin_entry.insert(END, t))
            self.button.grid(column=col, row=row, padx=20, pady=20)

    def MENU_OPTION(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.configure(padx=200, pady=150, bg=THEME_COLOR)
        self.window.geometry("4000x4000")
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
                                  font=("Ariel", 20, "bold"), command=self.WELCOME)
        self.exit_button.grid(column=2, row=4, pady=10)

    def WITHDRAW(self):

        self.DESTROY_WIDGET()
        self.CREATE_NUMBER_BUTTON()
        self.window.configure(padx=150, pady=100, bg=THEME_COLOR)
        self.window.geometry("4000x4000")
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
                                     command=self.WITHDRAW_AMOUNT, bg=THEME_COLOR,
                                     fg="black", font=("Ariel", 24, "bold"))
        self.confirm_button.grid(column=5, row=2, padx=20, pady=10)

        self.clear_button = Button(text="CLEAR", width=10, fg="black",
                                   bg=THEME_COLOR, font=("Ariel", 24, "bold")
                                   ,command=self.CLEAR_WITHDRAWAL_ENTRY)
        self.clear_button.grid(column=5, row=3, padx=20, pady=10)

        self.back_button = Button(text="BACK", width=10, bg=THEME_COLOR, fg="black",
                                  font=("Ariel", 24, "bold"), command=self.WELCOME)
        self.back_button.grid(column=5, row=4, pady=20, padx=20)

    def DEPOSIT(self):
        self.DESTROY_WIDGET()
        self.window.configure(padx=200, pady=100, bg=THEME_COLOR)
        self.window.geometry("4000x4000")
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
                                     fg="black", font=("Ariel", 20), command=self.PROCESS_DEPOSIT)
        self.Deposit_button.grid(column=5, row=2, padx=20, pady=20)

        self.clear_button = Button(text="CLEAR", width=10, fg="black", bg=THEME_COLOR, font=("Ariel", 20))
        self.clear_button.grid(column=5, row=3, padx=20, pady=20)

        back_button = Button(text="BACK", width=10, bg=THEME_COLOR, fg="black",
                             font=("Ariel", 20), command=self.WELCOME)
        back_button.grid(column=5, row=4, pady=20, padx=20)

    def VIEW_TRANSACTION(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.configure(padx=150, pady=50, bg=THEME_COLOR)
        self.window.geometry("4000x4000")
        Time_Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction_text = Text(height=30, width=50)
        transaction_text.grid(padx=300, pady=10)

        try:
            with open("transaction_History.txt", "r") as file:
                transactions = file.readlines()
                for transaction in transactions:
                    transaction_text.insert(END, transaction)  # Insert each transaction into the Text widget
        except FileNotFoundError:
            transaction_text.insert(END, "No transaction history found.")

        close_button = Button(text="Close", command=self.WELCOME)
        close_button.grid(pady=5)

    def CLEAR_WITHDRAWAL_ENTRY(self):
        self.Withdrawal_entry.delete(0, END)
        
    def CLEAR_DEPOSIT_ENTRY(self):
        self.deposit_amount_entry.delete(0, END)

    def WITHDRAW_AMOUNT(self):

        self.LOAD_BALANCE()
        try:
            self.amount = int(self.Withdrawal_entry.get())
            self.Withdrawal_entry.delete(0, END)
            if self.amount % 100 == 0:
                pass
            else:
                self.SHOW_MESSAGE("Invalid amount entered")

            self.amount = float(self.amount)
            if self.amount <= 0:
                self.SHOW_MESSAGE("Please enter a valid amount!")
            elif self.amount > self.balance:
                self.SHOW_MESSAGE("Insufficient funds!")
            else:

                self.balance -= self.amount
                self.transactions.append({
                    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "description": "Withdrawal",
                    "amount": self.amount,
                    "Balance": self.balance
                })
                self.TIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("transaction_History.txt", "a") as file:
                    file.write(f"{self.TIME_NOW} | Withdraw amount {self.amount} | Your Balance {self.balance}\n")
                self.SAVE_BALANCE()
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=self.my_email, password=self.password)
                    connection.sendmail(
                        from_addr=self.my_email,
                        to_addrs="sivam4266@gmail.com",
                        msg=f"subject: you done a withdrawal recently.\n\n{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} your withdrawal amount: {self.amount} your balance: {self.balance} "
                    )
        except ValueError:
            self.SHOW_MESSAGE("Invalid amount!")

    def PROCESS_DEPOSIT(self):

        self.LOAD_BALANCE()
        self.amount = int(self.deposit_amount_entry.get())
        self.deposit_amount_entry.delete(0, END)
        print(self.amount)
        if self.amount % 100 == 0:
            try:
                self.amount = float(self.amount)
                if self.amount <= 0:
                    raise ValueError("Deposit must be positive.")
                # Update balance and record transaction
                self.balance += self.amount
                self.transactions.append({
                    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "description": "Deposit",
                    "amount": self.amount,
                    "Balance": self.balance
                })
                self.TIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("transaction_History.txt", "a") as file:
                    file.write(f"{self.TIME_NOW} | Deposit amount {self.amount} | Your Balance {self.balance}\n")
                self.SAVE_BALANCE()
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=self.my_email, password=self.password)
                    connection.sendmail(
                        from_addr=self.my_email,
                        to_addrs="sivam4266@gmail.com",
                        msg=f"subject: you done a deposit recently.\n\n{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} your Deposit amount: {self.amount} your balance: {self.balance}")


            except ValueError as e:
                self.messagebox.showerror("Invalid input", str(e))
        else:
            self.messagebox.showwarning("Input required", "Please enter a valid deposit amount.")

    def LOAD_BALANCE(self):

        try:
            with open('balance.json', 'r') as file:
                data = json.load(file)
                self.balance = data.get('balance', 0)
                self.transactions = data.get('transactions', [])
        except FileNotFoundError or ValueError:
            self.balance = 0
            self.transactions = []

    def SAVE_BALANCE(self):
        """with open('balance.json', 'w') as file:
            json.dump({
                "balance": self.balance,
                "transactions": self.transactions
            }, file, indent=4)"""



    def SHOW_BALANCE(self):
        self.LOAD_BALANCE()
        balance_message = f"Your balance is: ${self.balance:.2f}"
        self.SHOW_MESSAGE(balance_message)

    def SHOW_MESSAGE(self, message:str):
        # Clear existing widgets
        self.DESTROY_WIDGET()

        message_label = Label(text=message, width=100, bg=THEME_COLOR, fg="white", font=("Ariel", 28, "bold"))
        message_label.pack(pady=20)

        back_button = Button(text="Back", bg=THEME_COLOR, fg="black", font=("Ariel", 24), command=self.WELCOME)
        back_button.pack(pady=10)

    def DESTROY_WIDGET(self):
        for widget in self.window.winfo_children():
            widget.destroy()