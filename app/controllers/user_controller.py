from app import db, app
from app.models.user import User
from flask import request, jsonify
from email_validator import validate_email, EmailNotValidError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


@app.post("/register")
def regester():
    data = request.get_json()

    # -----------email  validation----------
    try:
        valid = validate_email(data["email"])
        email = valid.email  # normalized email

    except EmailNotValidError as e:
        return jsonify(message=f"invalide email: {str(e)}."), 400

    # ----------password validation------------
    if len(data["password"]) < 6:
        return jsonify(message="Password must be 6 charachters long."), 400

    # ------------Hash password--------------
    hashed_password = generate_password_hash(data["password"], method="pbkdf2:sha256")

    # -----------------Create new user----------------------
    new_user = User(
        fname=data["fname"],
        lname=data["lname"],
        email=data["email"],
        password=hashed_password,
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="New user added successfully!."), 200


@app.post("/login")
def login():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalide or missing json data."}), 400

    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email).first()
    if not user and not check_password_hash(user.password, password):
        return {"message": "Bad password or user name!."}, 404
    access_token = create_access_token(identity=email)
    return {"message": "successful login!.", "access token": access_token}
