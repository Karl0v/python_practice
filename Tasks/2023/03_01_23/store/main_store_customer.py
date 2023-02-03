from store import Store
from customer import Customer

stock = list()
all_stores = list()
stock.append(Store(name='Allo', product='TV', price=500, qty=2))
stock.append(Store(name='Moyo', product='TV', price=800, qty=1))
stock.append(Store(name='Rozetka', product='Xbox', price=1500, qty=3))
stock.append(Store(name='Rozetka', product='Phone', price=499, qty=2))
stock.append(Store(name='Allo', product='Phone', price=580,qty=1))
stock.append(Store(name='Moyo', product='Headphones', price=300, qty=0))
stock.append(Store(name='Rozetka', product='Headphones', price=89, qty=5))
stock.append(Store(name='Allo', product='Watch', price=390, qty=2))
stock.append(Store(name='Moyo', product='Notebook', price=1300, qty=4))

customer = Customer(name='Abraham', account=3500)

print(stock[1])