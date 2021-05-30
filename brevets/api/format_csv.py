import flask

def csv_form(db, k, all="all"):
    entries = db.tododb.find()
    if k == -1:
        k = entries.count()
    open = ['Open']
    close = ['Close']
    for i in entries:
        open.append(i['open'])
        close.append(i['close'])
    response = []
    open = open[0:k+1]
    close = close[0:k+1]
    if all == "all":
        for i in range(len(open)):
            response.append(open[i])
        for j in range(len(close)):
            response.append(close[j])
    if all == "open":
        for i in range(len(open)):
            response.append(open[i])
    if all == "close":
        for i in range(len(close)):
            response.append(close[i])
    return ",".join(response)

def json_form(db, k, all="all"):
    entries = db.tododb.find()
    if k == -1:
        k = entries.count()
    open = []
    close = []
    for i in entries:
        open.append(i['open'])
        close.append(i['close'])
    open = open[0:k]
    close = close[0:k]
    response = {'Open':open, 'Close':close}
    if all == "open":
        del response['Close']
    if all == "close":
        del response['Open']
    return flask.jsonify(response)