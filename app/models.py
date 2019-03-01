from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship("Pitches", backref="user", lazy = "dynamic")
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'
        
# pitch class ................

class Pitches(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    description= db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def clear_pitches(cls):
        Pitches.all_pitches.clear()

    @classmethod
    def get_pitches(id):

        pitches = Pitches.query.all()
        return pitches



# comments class..........

class Comments(db.Model):
    __tablename__ = 'comments'


    id = db.Column(db. Integer, primary_key=True)
    comments = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self,id):

    
        comment = Comments.query.order_by(Comments.time_posted.desc()).filter_by(pitches_id=id).all()

        return comment




    






  








