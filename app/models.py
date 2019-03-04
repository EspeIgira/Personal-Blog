from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog:
    

    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote
   





class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    quotes_id=db.relationship("Quotes", backref="user", lazy = "dynamic")
    comments_id=db.relationship("comments", backref="user", lazy = "dynamic")
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
        


class Quotes(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer,primary_key = True)
    quote= db.Column(db.String)
    Comments_id = db.Column(db.Integer,db.ForeignKey("comments.id"))
    commentquote = db.relationship("Comments", backref="quote", lazy = "dynamic")
    


    def save_quote(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def clear_quotes(cls):
        Quotes.all_quotes.clear()

    @classmethod
    def get_quotes(id):

        quotes = Quotes.query.all()
        return quotes





# comments class..........

class Comments(db.Model):
    __tablename__ = 'comments'


    id = db.Column(db. Integer, primary_key=True)
    comments = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    quotes_id = db.Column(db.Integer, db.ForeignKey("quotes.id"))


    def save_comments(self):
        db.session.add(self)
        db.session.commit()


    def delete_comments(self):
        db.session.add(self)
        db.session.commit()

    def update_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comments.all_comments.clear()

    @classmethod
    def get_comments(id):

    
        comments = Comments.query.order_by(Comments.time_posted.desc()).filter_by(quotes_id=id).all()

        return comments



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Subscribe(UserMixin,db.Model):
    __tablename__ = 'subscribe'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    


    def save_subscribe(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_subscribe(self,id):

    
        comments = Comments.query.order_by(Comments.time_posted.desc()).filter_by(quotes_id=id).all()

        return comments

    def __repr__(self):
        return f'User {self.username}'
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
    




  








