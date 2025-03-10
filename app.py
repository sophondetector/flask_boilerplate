from flask import Flask, render_template, request, jsonify
from app_modules import make_response

PORT = 5000
HOST = 'localhost'
DEBUG = True

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/endpoint')
def endpoint():
    query = request.args['query']
    resp = make_response(query)
    return jsonify(resp)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    # db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
