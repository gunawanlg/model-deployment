
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit', method=['POST'])
def get_data():
    path_f1 = request.form['feature1']
    return path_f1

if __name__ == "__main__":
    app.run(port=8000, debug=True)