from main import db
from models.users import Users

# Create a linking table for a many-to-many relationship
portfolios = db.Table(
    'portfolios',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('ticker_id', db.String(45), db.ForeignKey('tickers.ticker_id'), primary_key=True)
)
# Create a linking table for a many-to-many relationship

class Tickers(db.Model):
    __tablename__ = "tickers"
    ticker_id = db.Column(db.String(45), primary_key=True)
    company_name = db.Column(db.String(45), unique=True, nullable=False)
    sector = db.Column(db.String(200))
    marketCap = db.Column(db.Integer)

    
    investors = db.relationship(
        Users,
        secondary=portfolios,
        backref=db.backref('followers')
    )
