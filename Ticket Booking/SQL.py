import sqlite3
import datetime

class SQL:
    def __init__(self):
        self.connection = sqlite3.connect("Booking.db")
        self.cursor = self.connection.cursor()


    # Password Generator Project

    def initialize(self):
    # SQL code to create an Account table for an ATM-Machine
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ticket_Price (
            S_No INTEGER Primary Key AUTOINCREMENT,
            Pickup_Location TEXT NOT NULL,
            Destination_Location TEXT NOT NULL,
            Ticket_Price INTEGER NOT NULL DEFAULT 0
        );
        ''')
        self.connection.commit()


    def Create_Booking(self, Pickup_Location:str, Destination_Location:str, Ticket_Price:int):
        #Booking_Time = datetime.datetime.now().strftime('%Y-%m-%d')
        self.cursor.execute('''
        INSERT INTO Ticket_Price (Pickup_Location, Destination_Location, Ticket_Price) 
        VALUES (?,?,?)
        ''', (Pickup_Location,Destination_Location,Ticket_Price))
        self.connection.commit()

    # Method to create the Transaction table
    """def initialize_transactions(self):
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
        self.connection.commit()"""