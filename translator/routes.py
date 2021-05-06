from flask import render_template
from translator import app
from translator.forms import TranslatorForm

@app.route("/", methods=["GET", "POST"])
@app.route("/home")
def index():
	form = TranslatorForm()
	return render_template("index.html", form=form)

