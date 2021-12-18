from main import db

class Usage(db.Model):

    __tablename__ = "usage"
    instance_id = db.Column(db.Integer, primary_key=True)
    no_logins = db.Column(db.Integer)
    

    def __init__(self):
        self.instance_id = 1
        self.no_logins = 0