from market.models import db
db.drop_all()
db.create_all()

from market.models import User, Item
u1 = User(username="Satvik", email = "satiknema@gmail.com", password_hash = "12345")
db.session.add(u1)
db.session.commit()

i1 = Item(name="IPhone 13", description = "Expensive af", barcode = "345678", price = "7257284")
i2 = Item(name="laptop", description = "decs2", barcode = "987654", price = "42937")
db.session.add_all([i1, i2])
db.session.commit()

i1.owner = User.query.filter_by(username="Satvik").first().id
db.session.add(i1)
db.session.commit()