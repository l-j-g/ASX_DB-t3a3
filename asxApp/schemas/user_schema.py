from main import ma
from models.users import Users
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields, exceptions, validate
from werkzeug.security import generate_password_hash


class UserSchema(ma.SQLAlchemyAutoSchema):

    # dump only, imformed only by the database.
    id = auto_field(dump_only=True)
    # Import appropriate validator and add check.
    username = auto_field(required=True, validate=validate.Length(min=1))
    # This type of field will get its value based on a function
    password = fields.Method(
        require=True,
        # never return this value, write only.
        load_only=True,
        deserialize="load_password"
    )

    tickers_followed = ma.Nested(
        "TickerSchema",
        only=("ticker_id", "company_name"),
        many = True
    )

    def load_password(self, password):
        if len(password) >= 6:
            return generate_password_hash(password, method='sha256')
        raise exceptions.ValidationError(
            "Password must be at least 6 characters"
            )

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
