import datetime

from magic-power import app


@app.route('/', methods = ['GET'])
def hello_world():
    return jsonify({'message': 'Welcome to MP, Magic Power!'})

@app.route('/datetime', methods = ['GET'])
def get_datetime():
    return jsonify({'datetime': str(datetime.datetime.now())})
