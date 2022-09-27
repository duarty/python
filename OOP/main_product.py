from product import Product;
##getters & setters
product1 = Product('Shirt', 100);
product1.discount(10);
print(product1.name, product1.price);

product2 = Product('Short','R$50');
product2.discount(20);
print(product2.name, product2.price)
