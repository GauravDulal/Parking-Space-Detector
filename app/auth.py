from flask import Blueprint, render_template, redirect, url_for, flash, request , jsonify
from .forms import LoginForm
from .models import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from . import db, login_manager
import pickle

auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(Amail=form.email.data).first()
        if user and check_password_hash(user.Apass, form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)

@auth.route('/status')
def status():
    try:
        with open('parking_status.pkl', 'rb') as file:
            parking_status = pickle.load(file)
        return jsonify(parking_status)
    except FileNotFoundError:
        return jsonify({"error": "Parking status file not found."}), 404

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
