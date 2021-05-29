from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return render_template('index.html')

@app.route('/everything')
def everything():
    r = requests.get('http://restapi:5000/listAll')
    return r.text

@app.route('/open')
def open():
    r = requests.get('http://restapi:5000/listOpen')
    return r.text

@app.route('/close')
def close():
    r = requests.get('http://restapi:5000/listClose')
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
