from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from website import get_sneakers


views = Blueprint('views', __name__)

@views.route('/')
def home():
    Allsneakers = get_sneakers()
    return render_template('home.html', user=current_user, sneakers = Allsneakers)

@views.route('/shoeEntry')
def entry():
    return render_template("shoeEntry.html", user=current_user)
