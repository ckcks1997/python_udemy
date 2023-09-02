import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})
class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] == "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        if df.loc[df["id"] == self.hotel_id, "available"].squeeze() == "yes":
            return True
        else:
            return False
        pass

class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel_obj = hotel_obj
    def generate(self):
        content = f"""
            Thank you,
            Name: {self.customer_name}
            Hotel:{self.hotel_obj.name}
        """
        return content

print(df)
hotel_id = input("enter id of the hotel")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("enter name:")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())

else:
    print("hotel is not free")