from customer import Customer


class Store:

    def __init__(self, name: str, product: str, price: int, qty: int):
        self.name = name
        self.product = product
        self.price = price
        self.qty = qty

    def __str__(self):
        return f'{self.name} - {self.product} - {self.price} USD'

    def hz(self):
        dict_stock = {'name': self.name,'product': self.product, 'price': self.price, 'qty': self.qty}






