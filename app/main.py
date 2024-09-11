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

@main.route('/live')
def live():
    try:
        result = subprocess.run(
            ['venv/Scripts/python', 'app_main.py'],
            check=True, 
            capture_output=True, 
            text=True
        )
        return redirect(url_for('main.index'))
    except subprocess.CalledProcessError as e:
        return jsonify({
            "message": "An error occurred",
            "error": str(e),
            "stderr": e.stderr,
            "suggestion": "It seems like the 'cv2' module is missing. Run 'pip install opencv-python' to install it."
        }), 500
    except FileNotFoundError as e:
        return jsonify({
            "message": "Script not found",
            "error": str(e)
        }), 404


    
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

def get_total_money():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT ROUND(SUM(cost),2) FROM log')
    total_money = cursor.fetchone()[0]
    conn.close()
    return total_money

@main.route('/get_total_money')
def get_total_money_route():
    total_money = get_total_money()
    return jsonify(total_money=total_money)

def get_times(space_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Execute query
        cursor.execute('SELECT entry_time, exit_time FROM payment WHERE space_id = %s', (space_id,))
        
        # Fetch the result (fetchone will fetch a single record)
        times = cursor.fetchone()

        # Ensure all results are processed before closing the cursor
        cursor.fetchall()  # Use this to clear any remaining unread results if necessary

        if times:
            entry_time, exit_time = times
            return entry_time, exit_time
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        # Ensure cursor and connection are closed after the fetch
        cursor.close()
        conn.close()
    
@main.route('/get_start_time', methods=['POST'])
def fetch_times():
    slot_number = request.form['slot_number']
    times = get_times(slot_number)
    if times:
        entry_time, exit_time = times
        # Convert timedelta to hours, minutes, and seconds
        entry_total_seconds = entry_time.total_seconds()
        entry_hours, remainder = divmod(entry_total_seconds, 3600)
        entry_minutes, entry_seconds = divmod(remainder, 60)
        formatted_entry_time = f"{int(entry_hours):02}:{int(entry_minutes):02}:{int(entry_seconds):02}"

        exit_total_seconds = exit_time.total_seconds()
        exit_hours, remainder = divmod(exit_total_seconds, 3600)
        exit_minutes, exit_seconds = divmod(remainder, 60)
        formatted_exit_time = f"{int(exit_hours):02}:{int(exit_minutes):02}:{int(exit_seconds):02}"
        time_difference_seconds = (exit_time - entry_time).total_seconds()
        time_difference_hours = time_difference_seconds / 3600
        total_money = round(time_difference_hours * 100, 2)
        return render_template('payment.html', entry_time=formatted_entry_time, exit_time=formatted_exit_time, time_difference=time_difference_seconds, total_money=total_money )
    else:
        return 'Slot number not found', 404