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
        backref=('followed_companies')
#        lazy='joined'
    )


    def __init__(self, ticker_id, company_name, sector, marketcap):
        self.ticker_id = ticker_id
        self.company_name = company_name
        self.sector = sector
        self.marketcap = marketcap
#        self.info = 1
#        self.info = info
'''
class Info(db.Model):
    __tablename__ = "info"
    id = db.Column(db.Integer, primary_key=True)
    ticker_id = db.Column(db.String(45), ForeignKey('tickers.ticker_id'))
    ticker = db.relationship("tickers", back_populates="child")
    def __init__(self, *args, **kwargs):
        for arg in kwargs.values:
            self.kwargs = self.arg
'''
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

