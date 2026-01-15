from app import ma
from marshmallow import fields

class CountrySchema(ma.Schema):
    Country_ID= fields.Int()
    Country_name=fields.Str()
    Capital=fields.Str()
    Erea=fields.Str()
    class Meta:
        fields=('Country_ID', 'Country_name', 'Capital', 'Erea')


country_schema=CountrySchema()
countries_schema=CountrySchema(many=True)
