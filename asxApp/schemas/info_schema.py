from marshmallow import fields
from main import ma
from models.tickers import Info
from marshmallow_sqlalchemy import auto_field


class InfoSchema(ma.SQLAlchemyAutoSchema):
    
    id = auto_field(dump_only=True)
    ticker_id = auto_field(dump_only=True)
    zipcode = auto_field(dump_only=True)
    sector = auto_field(dump_only=True)
    longBusinessSummary = auto_field(dump_only=True)
    city = auto_field(dump_only=True)
    phone = auto_field(dump_only=True)
    state = auto_field(dump_only=True)
    compensationAsOfEpochDate = auto_field(dump_only=True)
    country = auto_field(dump_only=True)
    website = auto_field(dump_only=True)
    maxAge = auto_field(dump_only=True)
    address = auto_field(dump_only=True)
    industry = auto_field(dump_only=True)

    tickers = ma.Nested("TickerSchema")

    # Metadata for the class 
    class Meta:
        # This schema applies to the 'Tickers' model
        model = Info
        # De-serialize the data to an instance of the model
        load_instance = True 

info_schema = InfoSchema()
infos_schema = InfoSchema(many=True)