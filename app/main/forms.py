from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PredictionForm(FlaskForm):
	sepal_length = StringField('Sepal Length', validators=[DataRequired()])
	sepal_width = StringField('Sepal Width', validators=[DataRequired()])
	petal_length = StringField('Petal Length', validators=[DataRequired()])
	petal_width = StringField('Petal Width', validators=[DataRequired()])
	submit = SubmitField('Predict')