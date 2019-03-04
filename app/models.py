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
    blogs=db.relationship("Blogs", backref="user", lazy = "dynamic")
    comments_id=db.relationship("Comments", backref="user", lazy = "dynamic")
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
        


class Blogs(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    quote= db.Column(db.String)
    author= db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship("Comments", backref="blogs", lazy = "dynamic")
    
    def save_Blogs(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def clear_Blogs(cls):
        Blogs.all_quotes.clear()

    @classmethod
    def get_Blogs(id):

        blogs = Blogs.query.all()

        return blogs




class Comments(db.Model):
    __tablename__ = 'comments'


    id = db.Column(db. Integer, primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blogs_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    
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
    def get_comments(cls,id):

    
        comment = Comments.query.filter_by(blogs_id=id).all()

        return comment




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
        comments = Comments.query.order_by(Comments.time_posted.desc()).filter_by(blogs_id=id).all()

        return comments

    def __repr__(self):
        return f'User {self.username}'


        
class Quote:
    
    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote
   
    
    




  








