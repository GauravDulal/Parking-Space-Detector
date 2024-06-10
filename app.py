from flask import Flask, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/parking_status', methods=['GET'])
def parking_status():
    try:
        with open('parking_status.pkl', 'rb') as file:
            status = pickle.load(file)
        return jsonify(status)
    except FileNotFoundError:
        return jsonify({"error": "Status file not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
