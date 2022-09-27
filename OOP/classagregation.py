# in class assossiation has two another mothagregation
class BuyCart:
    def __init__(self):
        self.products = []
    
    def insert_product(self, product):
        self.products.append(product);

    def product_list(self):
        for product in self.products:
            print(product.name, product.price);
    
    def total_sum(self):
        total = 0;
        for product in self.products:
            total += product.price
        return print(total)

class Product:
    def __init__(self, name, price):
        self.name = name;
        self.price = price;