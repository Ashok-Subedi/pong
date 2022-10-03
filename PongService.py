from flask import Flask, jsonify, request
from flask_httpauth import HTTPDigestAuth
import random

app = Flask(__name__)
auth = HTTPDigestAuth()
app.config['SECRET_KEY'] = 'secret key here'

credentials = {
    'vcu': 'rams'
}

@auth.get_password
def get_pw(username):
    if(username in credentials):
        return credentials.get(username)
    return None

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'page not here'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message': 'Something is Broken'}), 500

@app.route('/pong', methods=['GET'])
@auth.login_required
def do_pong():
    random_number = random.randint(1,99)
    return jsonify({
            "random_number": random_number
        })