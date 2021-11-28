"""
class Student:
    def __init__(self, name, grades) -> None:
        self.name=name
        self.grades = grades
    
    def average(self):
        gradesArr = self.grades
        return sum(gradesArr)/len(gradesArr)
    
    def __repr__(self) -> str:
        return f'<name: {self.name}, grades:{self.grades}>'
    
    def instance_method(self):
        print(f'called instance method of {self}')


student = Student("Satvik", (90, 95, 95, 95, 100))
student.instance_method()

"""
class Store:
    def __init__(self, storeName, items=[]) -> None:
        self.name = storeName
        self.items = items

    def __repr__(self) -> str:
        return f'<"{self.name}, items: {self.items}">\n'
    
    def add_item(self, **kwargs):
        self.items.append(kwargs)

    def stock_price(self):
        prices = list(map(lambda x:x['price'], self.items))
        return sum(prices)

    @classmethod
    def franchise(cls, store):
        return cls(store.name+" - Franchise", store.items)

    @staticmethod
    def store_details(store) -> str:
        return f'"{store.name}, items: {store.items}">'

store1 = Store("Nike")
store1 = Store.franchise(store1)
store1.add_item(name="Tshirt", price=50)
store1.add_item(name="shoes", price=100)
store1.add_item(name="Watch", price=10)

store2 = Store("Hogwarts")
store2.add_item(name="Wand", price=500)
store2.add_item(name="Cloak", price=1000)
store2.add_item(name="Pet", price=750)

store3 = Store("Garmin")
store3.add_item(name="watch", price=400)
store3.add_item(name="heart rate monitor", price=250)
store3 = Store.franchise(store3)


print(store1, store1.stock_price())
print()

print(store2, store2.stock_price())
print()

print(store3, store3.stock_price())
print("woa11h")

