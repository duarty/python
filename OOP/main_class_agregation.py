from classagregation import BuyCart, Product;

cart = BuyCart();
product1 = Product('T-Shirt', 50);
product2 = Product('Steam Key', 69);

cart.insert_product(product1);
cart.insert_product(product2);
cart.total_sum();
cart.product_list()