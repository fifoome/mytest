from flask import Flask
from flask import request
import json
from flask import jsonify
import requests
import logging

try:
    with open("/etc/config/config.json", "r") as f:
    # with open("./config.json", "r") as f:
        parsed_json = json.loads(f.read())
except:
    parsed_json = {
  "backend": "127.0.0.1",
  "backendPort": "80"
}
    print("failed configfile")

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def ma():
    d = {
        "title": "Hey, I am the frontend!",
        "backend data": "try /test"}
    return jsonify(d)

@app.route('/test')
def hello_world():
    try:
        r = requests.get(url = "http://" + parsed_json["backend"] + ":" + parsed_json["backendPort"] + "/test")
        data = r.json()
        # data = {}
    except:
        data = {"failed": "to connect to backend"}
        return data
    # extracting data in json format

    d = {
        "title": "Hey, I am the frontend!",
        "backend data": data}

    str = '''
            <div>
                <h2><strong>I am the frontend of this project</strong></h2>
        <p>&nbsp;</p>
        <p><strong>I can be queried by going to fifoome.com, which redirect to the ingress (nginx controller do the reverse proxy)</strong></p>
        <p><strong>My backend service is located at: %s</strong></p>
        <p><strong>A service (or svc) in k8s is an object that allows to have a static dns name and loadbalancing for a predefined group of pods (such as frontend or backend pod)</strong></p>
        <p><strong>When quering %s, the backend will query redis service at %s</strong></p>
        <p><strong>and will try to see if it can retrieve a key-value pair I set previously.</strong></p>
        <p><strong>the value of the pair is: %s</strong></p>
        <p>&nbsp;</p>
        <p><strong>Diagram:</strong></p>
        <p><strong><img src="./static/image.png" alt=""  /></strong></p>
        <p>&nbsp;</p>
        <p><strong><img src="./static/image2.png" alt=""  /></strong></p>
        </div>
        ''' % ("http://" + parsed_json["backend"] + ":" + parsed_json["backendPort"], "http://" + parsed_json["backend"] + ":" + parsed_json["backendPort"] + "/test", data["redis"], data["redis_key"])
    print str

    return str


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=80)
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()
