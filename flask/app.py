from flask import Flask
from flask import request
import redis, toml

with open("/etc/config/config.toml", "r") as f:
    parsed_toml = toml.loads(f.read())

r = redis.Redis(
    host=parsed_toml["alias"]['redis'],
    port=parsed_toml["alias"]['redisport'],
    password='')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container! \nthe value in redis is: ' + str(r.get("mykey"))

@app.route('/setdata')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    r.set("mykey", request.args.get('data'))
    return 'Set the key'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
