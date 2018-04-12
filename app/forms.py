from wtforms import TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf import Form



class UploadForm(Form):
	description= TextAreaField('Description',validators=[DataRequired()])
	photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only')])