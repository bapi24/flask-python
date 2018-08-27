class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return store+" - franchise"

    @staticmethod
    def store_details(store):
        return 'Name, tota'
        # Return a string representing the argument


store = Store("Amazon")
store.add_item("keyboard", 160)
Store.franchise(store)
Store.store_details(store)
