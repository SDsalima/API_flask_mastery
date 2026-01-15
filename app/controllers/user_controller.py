from app import db, app
from app.models.user import User
from flask import request, jsonify
from email_validator import validate_email, EmailNotValidError
from werkzeug.security import generate_password_hash


@app.post("/register")
def regester():
   data = request.get_json()
   
   #-----------email  validation----------
   try:  
      valid= validate_email(data['email'])
      email= valid.email      #normalized email
      
   except EmailNotValidError as e:
      return jsonify(message=f"invalide email: {str(e)}."), 400
   
   #----------password validation------------
   if len(data["password"])<6:
      return jsonify(message="Password must be 6 charachters long."), 400
   
   #------------Hash password--------------
   hashed_password = generate_password_hash(data["password"], method="pbkdf2:sha256")
   
   #-----------------Create new user----------------------
   new_user = User(
      fname=data["fname"],
      lname=data["lname"],
      email=data["email"],
      password=hashed_password,
   )
   
   db.session.add(new_user)
   db.session.commit()
   return jsonify(message='New user added successfully!.'), 201