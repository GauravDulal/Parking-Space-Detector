from flask import Flask, render_template, jsonify, request, flash
import pickle

app = Flask(__name__)

@app.route('/login' , methods=['GET','POST'])
def login():
    # data = request.form
    # print(data)
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/status')
def status():
    try:
        with open('parking_status.pkl', 'rb') as file:
            parking_status = pickle.load(file)
        return jsonify(parking_status)
    except FileNotFoundError:
        return jsonify({"error": "Parking status file not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
