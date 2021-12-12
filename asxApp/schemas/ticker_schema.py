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

    followers = ma.Nested(
        "UserSchema",
        only = ("id","username")
    )
    # Metadata for the class 
    class Meta:
        # This schema applies to the 'Tickers' model
        model = Tickers
        # De-serialize the data to an instance of the model
        load_instance = True

ticker_schema = TickerSchema()
tickers_schema = TickerSchema(many=True)
