from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,FloatField
from wtforms.validators import DataRequired

class EditBook(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators= [DataRequired()])
    num_pages  = StringField('Number of Pages', validators=[DataRequired()])
    submit = SubmitField('Update')

class CreateBook(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages = IntegerField('Number of pages', validators=[DataRequired()])
    avg_rating = FloatField('Rating', validators=[DataRequired()])
    img = StringField('Image', validators=[DataRequired()])
    author = StringField('Author')
    pub_id = IntegerField('Publisher id', validators=[DataRequired()])
    submit = SubmitField('Create')






