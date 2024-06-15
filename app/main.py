from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
import pickle

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html', name=current_user.Amail)

@main.route('/log')
@login_required
def log():
    return render_template('log.html')

@main.route('/checkout')
@login_required
def checkout():
    return render_template('checkout.html')

@main.route('/status')
def status():
    try:
        with open('parking_status.pkl', 'rb') as file:
            parking_status = pickle.load(file)
        return jsonify(parking_status)
    except FileNotFoundError:
        return jsonify({"error": "Parking status file not found."}), 404