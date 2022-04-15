from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required         # cant get to home page unless you login #
def home():
    return render_template("home.html")

