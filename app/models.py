from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'admin_creds'
    
    Aid = db.Column(db.Integer, primary_key=True)
    Amail = db.Column(db.String(150), unique=True, nullable=False)
    Apass = db.Column(db.String(150), nullable=False)

    def get_id(self):
        return self.Aid
