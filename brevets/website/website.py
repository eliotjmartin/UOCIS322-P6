from flask import Flask, render_template, request
import flask
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return render_template('index.html')

@app.route('/everything')
def everything():
    k = request.args.get("k", type=int) or -1
    csv = request.args.get("csv", type=str)
    app.logger.debug("k = {}".format(k))
    app.logger.debug("csv= {}".format(csv))
    if csv == None:
        r = requests.get(f'http://restapi:5000/listAll?top={k}')
    else:
        r = requests.get(f'http://restapi:5000/listAll/csv?top={k}')
    return r.text

@app.route('/open')
def open():
    k = request.args.get("k", type=int) or -1
    csv = request.args.get("csv", type=str)
    if csv == None:
        r = requests.get(f'http://restapi:5000/listOpenOnly?top={k}')
    else:
        r = requests.get(f'http://restapi:5000/listOpenOnly/csv?top={k}')
    return r.text

@app.route('/close')
def close():
    k = request.args.get("k", type=int) or -1
    csv = request.args.get("csv", type=str)
    if csv == None:
        r = requests.get(f'http://restapi:5000/listCloseOnly?top={k}')
    else:
        r = requests.get(f'http://restapi:5000/listCloseOnly/csv?top={k}')
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
