import datetime

from flask import jsonify

from magic_power import app
from magic_power.services import manage


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/', methods = ['GET'])
def hello_world():
    return jsonify({'message': 'Welcome to MP, Magic Power!'})

@app.route('/datetime', methods = ['GET'])
def get_datetime():
    return jsonify({'datetime': str(datetime.datetime.now())})

@app.route('/mp/v1/services', methods=['GET'])
def _list_services():
    """
    OSS API
    List services access
    ---
    tags:
      - Services
    """
    ret = manage.list_services()

    if not ret['Outcome']:
        raise InvalidUsage(ret['Cause'], status_code=503)
    return jsonify({'result': ret})
