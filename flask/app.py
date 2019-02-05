from flask import Flask
from flask import request
import redis, toml
from flask import jsonify



try:
    with open("/etc/config/config.toml", "r") as f:
    # with open("./config.toml", "r") as f:
        parsed_toml = toml.loads(f.read())
    r = redis.Redis(
        host=parsed_toml["alias"]['redis'],
        port=parsed_toml["alias"]['redisport'],
        password='')
except:

    r = None

app = Flask(__name__)

@app.route('/test')
def hello_world():

    if r == None:
        d = {
            "title": "Hey, we have Flask in a Docker container!",
            "redis_key": "failed",
            "redis": parsed_toml["alias"]['redis'] + ":" + parsed_toml["alias"]['redisport']
            }
    else:
        d = {
            "title": "Hey, we have Flask in a Docker container!",
            "redis_key": str(r.get("mykey")),
            "redis": parsed_toml["alias"]['redis'] + ":" + parsed_toml["alias"]['redisport']}
    return jsonify(d)

@app.route('/')
def ma():

    return "test"

@app.route('/setdata')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    r.set("mykey", request.args.get('data'))
    return 'Set the key'

if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()
