from main import ma
from models.tickers import Tickers
from marshmallow_sqlalchemy import auto_field


class TickerSchema(ma.SQLAlchemyAutoSchema):

    # dump only, imformed only by the database. 
    ticker_id = auto_field(dump_only=True)
    company_name = auto_field(dump_only=True)

    followers = ma.Nested(
        "UserSchema",
        only = ("id","username")
    )
    # Metadata for the class 
    class Meta:
        model = Tickers
        load_instance = True

ticker_schema = TickerSchema()
tickers_schema = TickerSchema(many=True)
