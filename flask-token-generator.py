from flask import Flask, request, jsonify, make_response
import datetime
import jwt

# Replace these with your details
CONSUMER_KEY = 'yourconsumerkey'
CONSUMER_SECRET = 'yourconsumersecret'

# Only change this if you're sure you know what you're doing
CONSUMER_TTL = 86400


def generate_token(user_id):
    return jwt.encode({
        'consumerKey': CONSUMER_KEY,
        'userId': user_id,
        'issuedAt': _now().isoformat() + 'Z',
        'ttl': CONSUMER_TTL
    }, CONSUMER_SECRET)


def _now():
    return datetime.datetime.utcnow().replace(microsecond=0)


app = Flask(__name__)


@app.route('/api/token', methods=["GET", "OPTIONS"])
def index():
    return generate_token("omerege_user_id")
    # if request.method == "OPTIONS":
    #     return _build_cors_preflight_response()
    # elif request.method == "GET":
    #     my_token = generate_token("omerege_user_id")
    #     return _corsify_actual_response(jsonify(my_token))
    # raise RuntimeError("We don't know how to handle method {}".format(request.method))


# def _build_cors_preflight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "localhost")
#     response.headers.add('Access-Control-Allow-Headers', "*")
#     response.headers.add('Access-Control-Allow-Methods', "*")
#     return response
#
#
# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin", "localhost")
#     return response


app.run(host='0.0.0.0', port=80)

