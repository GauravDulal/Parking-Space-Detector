from flask import Blueprint, render_template, jsonify, redirect, url_for, request
from flask_login import login_required, current_user 
import mysql.connector
import pickle
import subprocess

main = Blueprint('main', __name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'psds'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@main.route('/')
@login_required
def index():
    return render_template('index.html', name=current_user.Amail)

@main.route('/log')
@login_required
def log():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT log_id, space_id, log_time, entry_time, exit_time, cost,status,payment_status FROM log")
    logs = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('log.html', logs=logs)

@main.route('/delete/<int:log_id>', methods=['POST'])
@login_required
def delete(log_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM log WHERE log_id = %s", (log_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('main.log'))

@main.route('/checkout')
@login_required
def checkout():
    return render_template('checkout.html')

# @main.route('/live')
# def live():
#     try:
#         subprocess.run(['python', 'app_main.py'], check=True)
#         return "Main script executed successfully!"
#     except subprocess.CalledProcessError as e:
#         return f"An error occurred: {e}"
@main.route('/status')
def status():
    try:
        with open('parking_status.pkl', 'rb') as file:
            parking_status = pickle.load(file)
        return jsonify(parking_status)
    except FileNotFoundError:
        return jsonify({"error": "Parking status file not found."}), 404

def get_total_cars():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM log WHERE status="Entry"')
    total_cars = cursor.fetchone()[0]
    conn.close()
    return total_cars

@main.route('/get_total_cars')
def get_total_cars_route():
    total_cars = get_total_cars()
    return jsonify(total_cars=total_cars+59)