import json
from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__="usuarios"
    
    id=db.Column(db.Integer, primarykey=True)
    username=db.Column(db.String(50), unique=True,nullable=False)
    password_hash=db.Column(db.String(128), nullable=False)
    role=db.Column(db.String(50), nullable=False)
    
    def __init__(self, username, password, role=["user"]):
        self.username=username
        self.password_hash=generate_password_hash(password)
        self.role=json.dumps(role)
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod   
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    