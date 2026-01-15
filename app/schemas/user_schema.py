from app import ma
from marshmallow import fields


class UserSchema(ma.Schema):
    ID=fields.Int()
    fname=fields.Str()
    lname=fields.Str()
    email=fields.Str()
    password=fields.Str()
    class Meta:
        fields=('ID', 'fname', 'lname', 'email', 'password')
        

user_schema= UserSchema()
users_schema=UserSchema(many=True)