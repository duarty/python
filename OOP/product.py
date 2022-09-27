class Product:
    def __init__(self, name, price):
        self.name = name;
        self.price = price;
    
    def discount(self, percent):
        self.price =  self.price - (self.price * (percent / 100));

    @property
    def name(self):
        return self._name;

    @name.setter
    def name(self, value):
        self._name = value.title();

    #getter
    @property
    def price(self):
        return self._price

    #setter
    @price.setter
    def price (self, value):

        if isinstance(value, str):
            value = float(value.replace('R$', ''));
            
        self._price = value;