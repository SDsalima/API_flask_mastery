from app import db
from sqlalchemy import Column, String,Integer


class User(db.Model):
   __tablename__= 'Users'
   ID=  Column( Integer, primary_key= True)
   fname= Column( String(50), nullable= False)
   lname= Column( String(50), nullable= False)
   email=  Column( String(120), nullable=False, unique=True)
   password=  Column( String(700), nullable=False)

      