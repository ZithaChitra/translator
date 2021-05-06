from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class TranslatorForm(FlaskForm):
	input_text = TextAreaField("Sentence", validators=[DataRequired(), Length(max=40)])
	output_text = TextAreaField("Translation")
	submit = SubmitField("Translate")


class InputForm(FlaskForm):
	input_text = TextAreaField("Input Sentence", validators=[DataRequired()])
	submit = SubmitField("Translate")


class OutputForm(FlaskForm):
	output_text = TextAreaField("Translation")