from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UserForm(FlaskForm):

    title = StringField('Pitch Category',validators=[Required()])
    user = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class AddQuote(FlaskForm):

    comments = TextAreaField('comments', validators=[Required()])
    submit = SubmitField('Add comment')

    