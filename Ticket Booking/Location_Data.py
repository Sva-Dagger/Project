from SQL import SQL

Sql = SQL()

class Data:
    def __init__(self):
        self.Data1=[("Coimbatore", "Madurai", 160), ("Coimbatore", "Srivilliputhur", 100), ("Coimbatore", "Rajapalayam", 280),
                    ("Srivilliputhur", "Madurai", 100), ("Srivilliputhur", "Coimbatore", 240), ("Srivilliputhur", "Rajapalayam", 20),
                    ("Madurai", "Coimbatore", 160), ("Madurai", "Srivilliputhur", 100), ("Madurai", "Rajapalayam", 120),
                    ("Rajapalayam", "Coimbatore", 280), ("Rajapalayam", "Srivilliputhur", 240), ("Rajapalayam", "Madurai", 120),]

    def Price(self):
        for (Pickup_Location, Destination_Location, Ticket_Price) in self.Data1:
            Sql.Create_Booking(Pickup_Location, Destination_Location, Ticket_Price)

