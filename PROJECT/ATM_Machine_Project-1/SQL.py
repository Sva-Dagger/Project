import sqlite3
import datetime

class SQL:
    def __init__(self):
        self.connection = sqlite3.connect("Account.db")
        self.cursor = self.connection.cursor()


    # Password Generator Project

    def initialize(self, name:str):
    # SQL code to create an Account table for an ATM-Machine

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Account (
            Account_no INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each account, auto-incremented
            Account_opening TEXT NOT NULL DEFAULT (DATE('now')),  -- Sets current date by default
            Name TEXT NOT NULL,                            -- Name of the account holder
            Email TEXT NOT NULL,
            Password TEXT NOT NULL,                        -- Password for account access
            Balance REAL DEFAULT 0,                        -- Account balance, initialized to 0
            User_status TEXT DEFAULT 'Active'           -- Status of the account (e.g., 'Active', 'Inactive')
        );
        ''')
        self.connection.commit()


    def create_account(self, name:str, password:str, Email:str):
        initial_balance = 0
        initial_deposit = 0
        initial_withdrawn = 0
        user_status = "Active"
        account_opening_date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.cursor.execute('''
        INSERT INTO Account (Name, Email, Password, Balance, Account_opening, User_status) 
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, Email, password, initial_balance, account_opening_date, user_status))
        self.connection.commit()
        self.initialize_transactions()

    # Method to create the Transaction table
    def initialize_transactions(self):
        # SQL code to create a Transaction table for email-based transaction records
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS "Transaction" (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each transaction
                email TEXT NOT NULL,                               -- Email associated with the account
                transaction_type TEXT NOT NULL,                    -- Type of transaction: 'Deposit' or 'Withdrawal'
                amount REAL NOT NULL,                              -- Amount for the transaction
                timestamp TEXT NOT NULL                            -- Timestamp of the transaction
            );
        ''')
        self.connection.commit()

    # Method to record a deposit transaction

    def record_deposit(self, email: str, amount: float):
        transaction_type = "Deposit"
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert transaction record
        self.cursor.execute('''
            INSERT INTO "Transaction" (Email, Transaction_type, Amount, Timestamp) 
            VALUES (?, ?, ?, ?)
        ''', (email, transaction_type, amount, timestamp))

        # Update balance in the Account table
        self.cursor.execute('''
            UPDATE Account 
            SET Balance = Balance + ? 
            WHERE Email = ?
        ''', (amount, email))
        self.connection.commit()



    # Method to record a withdrawal transaction
    def record_withdrawal(self, email: str, amount: float):
        # Check if the balance is sufficient

        transaction_type = "Withdrawal"
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
                        INSERT INTO "Transaction" (Email, Transaction_type, Amount, Timestamp) 
                        VALUES (?, ?, ?, ?)
                    ''', (email, transaction_type, amount, timestamp))

            # Update balance in the Account table
        self.cursor.execute('''
                        UPDATE Account 
                        SET Balance = Balance - ? 
                        WHERE Email = ?
                    ''', (amount, email))
        self.connection.commit()