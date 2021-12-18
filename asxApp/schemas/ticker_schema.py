from marshmallow import fields
from main import ma
from models.tickers import Tickers 
from marshmallow_sqlalchemy import auto_field


class TickerSchema(ma.SQLAlchemyAutoSchema):

    # dump only, imformed only by the database. 
    ticker_id = auto_field(dump_only=True)
    company_name = auto_field(dump_only=True)
    sector = auto_field(dump_only=True)
    marketcap = auto_field(dump_only=True)

    info = ma.Nested(
       "InfoSchema",
       exclude=("tickers",)
    )
    

   # The schema of users that are following the ticker is nested inside the ticker schema 
    followers = ma.Nested(
        "UserSchema",
        # The use of 'only' prevents an infinite loop of nested schemas
        only = ("id","username"),
        many = True
    )
    # Metadata for the class 
    class Meta:
        # This schema applies to the 'Tickers' model
        model = Tickers
        # De-serialize the data to an instance of the model
        load_instance = True

ticker_schema = TickerSchema()
tickers_schema = TickerSchema(many=True)
# Partial schema, if we want to update some fields not all.
ticker_update_schema = TickerSchema(partial=True)

