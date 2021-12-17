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

    __tablename__ = "tickers"
    ticker_id = db.Column(db.String(45), primary_key=True)
    company_name = db.Column(db.String(45), unique=True, nullable=False)
    sector = db.Column(db.String(200))
    marketcap = db.Column(db.Integer)

# one-to-one relationship for tickers to their info 
    
    # The many-to-many relationship is being expressed through the association table called enrolments. 
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
#        self.info = 1
#        self.info = info
class Info(db.Model):
    __tablename__ = "info"
    ticker_id = db.Column(db.string(45), primary_key=True)

    zip =  db.Column(db.Integer)
    sector = db.Column(db.String(100))
    longBusinessSummary = db.Column(db.String(100))
    city = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    state = db.Column(db.String(100))
    compensationAsOfEpochDate = db.Column(db.String(100))
    country = db.Column(db.String(100))
    website = db.Column(db.String(100))
    maxAge = db.Column(db.String(100))
    address1 = db.Column(db.String(100))
    fax = db.Column(db.String(100))
    industry = db.Column(db.String(100))
    address2 = db.Column(db.String(100))

    def __init__(self, values):
        self.zip =  values[0]
        self.sector = values[1]
        self.longBusinessSummary = values[2]
        self.city = values[3]
        self.phone = values[4]
        self.state = values[5]
        self.compensationAsOfEpochDate = values[6]
        self.country = values[7]
        self.website = values[8]
        self.maxAge = values[9]
        self.address1 = values[10]
        self.fax = values[11]
        self.industry = values[12]
        self.address2 = values[13]
'''
class Cashflow(db.Model):
    __tablename__ = "cashflow"
    id = db.Column(db.Integer, primary_key=True)
    ticker_id = db.Column(db.String(45), ForeignKey('tickers.ticker_id'))
    ticker = db.relationship("tickers", back_populates="child")

    def __init__(self):
       pass 
        for arg in kwargs.values:
            self.kwargs = self.arg
'''

