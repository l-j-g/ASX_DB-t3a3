from sqlalchemy.sql.schema import ForeignKey
# from sqlalchemy.dialects import postgresql
from main import db
from models.users import Users

# Create a linking table for a many-to-many relationship
portfolios = db.Table(
    'portfolios',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('ticker_id', db.String(45), db.ForeignKey('tickers.ticker_id'), primary_key=True)
)

class Tickers(db.Model):
    """ Stores basic infomation about ASX listed companies"""
    __tablename__ = "tickers"
    ticker_id = db.Column(db.String(45), primary_key=True)
    company_name = db.Column(db.String(45), unique=True, nullable=False)
    sector = db.Column(db.String(200))
    marketcap = db.Column(db.Integer)

    # one-to-one relationship for tickers to their info 
    info = db.relationship("Info", back_populates='tickers', uselist=False)
    
    # The many-to-many relationship is being expressed through the association table called portfolios. 
    followers = db.relationship(
        Users,
        secondary=portfolios,
        backref=('followed_companies'),
        lazy='joined'
    )


    def __init__(self, ticker_id, company_name, sector, marketcap):
        self.ticker_id = ticker_id
        self.company_name = company_name
        self.sector = sector
        self.marketcap = marketcap

class Info(db.Model):
    """ Stores additional company infomation"""
    __tablename__ = "info"
    id = db.Column(db.Integer, primary_key=True)
    ticker_id = db.Column(db.String(45), ForeignKey('tickers.ticker_id'), unique=True)
    zipcode =  db.Column(db.String(45))
    sector = db.Column(db.String(500))
    longBusinessSummary = db.Column(db.String(1000))
    city = db.Column(db.String(500))
    phone = db.Column(db.String(500))
    state = db.Column(db.String(500))
    compensationAsOfEpochDate = db.Column(db.String(500))
    country = db.Column(db.String(500))
    website = db.Column(db.String(500))
    maxAge = db.Column(db.String(500))
    address = db.Column(db.String(500))
    industry = db.Column(db.String(500))

    # many-to-one side of info - ticker relationship
    
    tickers = db.relationship('Tickers', back_populates='info')

    def __init__(self, values, ticker_id):
        self.ticker_id = ticker_id
        self.zipcode = values[0]
        self.sector = values[1]
        self.longBusinessSummary = values[2]
        self.city = values[3]
        self.phone = values[4]
        self.state = values[5]
        self.compensationAsOfEpochDate = values[6]
        self.country = values[7]
        self.website = values[8]
        self.maxAge = values[9]
        self.address = values[10]
        self.industry = values[11]

