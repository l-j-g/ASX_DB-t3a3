from main import db

class Usage(db.Model):
    """ Stores infomation about website usage """
    __tablename__ = "usage"
    instance_id = db.Column(db.Integer, primary_key=True)
    # counts the number of logins that have occured
    no_logins = db.Column(db.Integer)
    

    def __init__(self):
        self.instance_id = 1
        self.no_logins = 0