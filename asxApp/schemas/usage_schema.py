from marshmallow import Schema, fields
from main import ma
from models.usage import Usage
from marshmallow_sqlalchemy import auto_field



class UsageSchema(Schema):
    # dump only, imformed only by the database. 
    instance_id = fields.Int()
    no_logins = fields.Int()

class Meta:
    model = Usage
    load_instance = True

usage_schema = UsageSchema()
usages_schema = UsageSchema(many=True)

