from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "kj32b3t5jy,4uenhgw3gq97ghq389pf4;B"

login_manager = LoginManager(app)
login_manager.login_view = "login"

from . import routes