from app import app, db, auth
from app.models.country import Country
from app.schemas.country_schema import country_schema, countries_schema
from flask import jsonify, request
from flask_jwt_extended import  jwt_required


@app.get('/countries')
@auth.verify_password
def countries():
    country_list=Country.query.all()
    result= countries_schema.dump(country_list)
    return jsonify(data=result)



@app.route("/country_details/<int:country_id>", methods=['GET'])
@jwt_required()
def country_details(country_id):
    country=Country.query.filter_by(Country_ID=country_id).first()
    if country:
        result= country_schema.dump(country)
        return jsonify(result)
    return jsonify("That country not exist!."), 404



# # post form data to the api
# @app.post('/add_country')
# @auth.verify_password
# def add_country():
#     country_name= request.['country_name']
#     check_name=Country.query.filter_by(Country_name= country_name).first()
#     if check_name:
#         return jsonify("That country is already exist in the database!."), 409
#     capital= request.form['capital']
#     erea= request.form['crea']
#     new_country= Country(Country_name=country_name,Capital=capital, Erea=erea)
#     db.session.add(new_country)
#     db.session.commit()
#     return jsonify("Your country is added successfully!."),201


# post json form
@app.route("/add_country1", methods=['POST'])
def add_country():
    data= request.get_json()
    if not data:
        return jsonify("Invalid or messing data!."), 400
    country_name= data.get('Country_name')
    checked_name= Country.query.filter_by(Country_name= country_name).first()
    if checked_name:
        return jsonify("This country is already exists in the database!."), 409
    capital= data.get('Capital')
    erea=data.get('Erea')
    new_country= Country(Country_name=country_name, Capital=capital, Erea=erea)
    db.session.add(new_country)
    db.session.commit()
    return jsonify("Your country is added successfully!."), 201

@app.route("/update_country/<int:country_id>", methods=['PATCH'])
@auth.verify_password
def update_country(country_id):
    data= request.get_json()
    country=Country.query.filter_by(Country_ID= country_id).first()
    if not country:
        return jsonify(message="Country not exist!."), 404
    
    if 'Country_name' in data:
        country.Country_name=data['Country_name']
    if 'Capital' in data:
        country.Capital=data['Capital']
    if 'Erea' in data:
        country.Erea=data['Erea']
    db.session.commit()
    return jsonify({"message":"Country updated successfully!","country_id": country_id}),200




@app.route("/remove_country/<int:country_id>", methods=['DELETE'])
@auth.login_required()
def remove_country(country_id):
    country=Country.query.filter_by(Country_ID=country_id).first()
    if not country:
        return jsonify(message="Country does not exist!."), 404
    
    db.session.delete(country)
    db.session.commit()
    return jsonify(message='Country deleted successfully!.'), 200
