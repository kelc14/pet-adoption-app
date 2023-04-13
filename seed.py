from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add pets to database

pet1 = Pet(name="Rodney", species="Dog", photo_url="https://cdn.mos.cms.futurecdn.net/ASHH5bDmsp6wnK6mEfZdcU-1200-80.jpg", age="2" )
pet2 = Pet(name="Sparky", species="Dog", photo_url="https://i.guim.co.uk/img/media/fe1e34da640c5c56ed16f76ce6f994fa9343d09d/0_174_3408_2046/master/3408.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=67773a9d419786091c958b2ad08eae5e", age="5" )
pet3 = Pet(name="Fluffy", species="Cat", photo_url="https://static.vecteezy.com/system/resources/previews/002/410/747/original/cute-siamese-cat-on-yellow-background-free-photo.jpg", age="8" )
pet4 = Pet(name="Tinker", species="Cat", photo_url="", age="2" )
pet5 = Pet(name="Mickey", species="Dog", photo_url="https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg", age="1" )


db.session.add_all([pet1, pet2, pet3, pet4, pet5])
db.session.commit()