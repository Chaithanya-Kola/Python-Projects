class Product:
    def __init__(self,Product_id,Name,Price,Qunatity):
        self.Product_id=Product_id
        self.Name=Name
        self.Price=Price
        self.Qunatity=Qunatity

    def display_Productinfo(self):
        print("--------"*3)
        print("***Product Details***")
        print("--------"*3)
        print(f"1.Product ID: {self.Product_id}")
        print(f"2.Name: {self.Name}")
        print(f"3.Price: {self.Price}")
        print(f"4.Quantity: {self.Qunatity}")
        print("--------"*3)
