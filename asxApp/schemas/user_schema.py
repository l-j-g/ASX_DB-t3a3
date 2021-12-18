from main import ma
from models.users import Users
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields, exceptions, validate, ValidationError
from werkzeug.security import generate_password_hash
from schemas.ticker_schema import TickerSchema


class UserSchema(ma.SQLAlchemyAutoSchema):

    # dump only, imformed only by the database.
    id = auto_field(dump_only=True) # Import appropriate validator and add check.
    username = auto_field(required=True, validate=validate.Length(min=6, max=200))
    # This type of field will get its value based on a function
    password = fields.Method(
        require=True,
        # never return this value, write only.
        load_only=True,
        deserialize="load_password"
    )
    followed_companies = ma.Nested(
        "TickerSchema", 
        only=("ticker_id", "company_name"),
        many=True
        )
    
    def load_password(self, password):

        #validator = validate.Regexp("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,32}$")
        numval = validate.Regexp("(?=.*[0-9])", error="Password must contain a number.")    
        lcval = validate.Regexp("(?=.*[a-z])", error="Password must contain lowercase letter.")    
        upval = validate.Regexp("(?=.*[A-Z])", error="Password must contain uppercase letter.")    
        lenval = validate.Regexp(".{6,32}", error="Password length must be between 6 and 32 characters.")

        validator = validate.And(numval,lcval,upval,lenval)

        if validator(password):
            return generate_password_hash(password, method='sha256')
        raise ValidationError
        
        
    # Metadata for the class
    class Meta:
        # This schema applies to the 'Users' model
        model = Users
        # De-serialize the data to an instance of the model
        load_instance = True

# Single user schema
user_schema = UserSchema()
# Multiple user schema
users_schema = UserSchema(many=True)
# Partial schema, if we want to update some fields, not all.
user_update_schema = UserSchema(partial=True)
