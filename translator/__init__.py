from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "408c9fa8057e46a76bacb5f9efd75493"

from translator import routes