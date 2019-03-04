from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email
from ..models import Subscribe

class CommentForm(FlaskForm):

   
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
   
    blog = TextAreaField('blog',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    


class SubscribeForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    name =  TextAreaField('add your username', validators=[Required()])
    submit = SubmitField('Submit')

