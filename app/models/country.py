from app import db
from sqlalchemy import Float,String,Integer, Column

class Country(db.Model):
   __tablename__="Countries"
   Country_ID= Column( Integer, primary_key= True)
   Country_name=  Column( String(100), nullable=False)
   Capital= Column( String(100))
   Erea= Column( Float)
   