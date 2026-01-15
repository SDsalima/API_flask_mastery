from app import db,app
from app.models.country import Country
from app.models.user import User


@app.cli.command("db_create")  
def db_create():
    db.create_all()
    print("DateBase created!.")
    
@app.cli.command("db_drop")
def db_drop():
    db.drop_all()
    print("DataBase dropped!.")  
   
   
@app.cli.command("db_seed")
def db_seed():
    usa=Country(Country_name="USA",
                Capital="Washington",
                Erea=3249.32456)
    germany=Country(Country_name="German",
                    Capital="Birlin",
                    Erea=3211459888)
    db.session.add(usa)
    db.session.add(germany)
    test_user=User(fname="salima",
                  lname="Dergoul",
                  email="test@test.com",
                  password="123456")
    
    db.session.add(test_user)
    db.session.commit()
    print("Database seeded!.")
    