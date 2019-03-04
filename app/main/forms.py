from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UserForm(FlaskForm):

   
    user = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class AddBlog(FlaskForm):

    comments = TextAreaField('comments', validators=[Required()])
    submit = SubmitField('Add comment')

    