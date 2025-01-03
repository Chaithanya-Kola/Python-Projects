class Customer:
    def __init__(self,Customer_id,Customer_name,Customer_address):
        self.Customer_id=Customer_id
        self.Customer_name=Customer_name
        self.Customer_address=Customer_address

    def display_Customerinfo(self):
        print("--------"*3)
        print("***Customer Details***")
        print("--------"*3)
        print(f"1.Customer_id: {self.Customer_id}")
        print(f"2.Customer_Name: {self.Customer_name}")
        print(f"3.Customer_address:{self.Customer_address}")
        print("--------"*3)

