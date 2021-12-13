from main import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(UserMixin, db.Model):

    __tablename__ = "users"
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        nullable=False
    )

    portfolio = db.relationship(
        'Ticker',
        
    )

    @property
    def image_filename(self):
        return f"user_images/{self.id}.png"

    # No init method needed, because we have a schema.

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)
        
# hide_parameters