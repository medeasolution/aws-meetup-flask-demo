from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from auth import login, identity

app = Flask(__name__)
jwt = JWT(app, login, identity)
app.config['JWT_SECRET_KEY'] = 'our_jwt_secret_key'
@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/secret')
@jwt_required()
def secret_method():
    return '%s' % current_identity


@app.route('/perform_calculations', methods=['POST'])
@jwt_required()
def perform_calculations():
    for _ in range(50000):
        with open('/dev/urandom', 'r') as f:
            c = f.read(1)
    return "operation complete"

@app.route('/status', methods=['GET'])
def status():
    return 'OK'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', threaded=True)
