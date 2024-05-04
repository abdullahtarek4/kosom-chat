from flask import Flask, render_template, jsonify
from data_analysis import load_boston_data

app = Flask(__name__)

# Route to load the Boston Housing dataset
@app.route('/load_boston_data')
def load_boston_data_route():
    df = load_boston_data()
    return jsonify(df.to_dict(orient='records'))

# Route for your index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
