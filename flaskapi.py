from flask import Flask, jsonify
from data import final_data

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Star Data API!'

@app.route('/stars', methods=['GET'])
def get_stars():
    return jsonify(final_data)

if __name__ == '__main__':
    app.run(debug=True)
