from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    switch = requests.get("http://example_switch_1:8000").content
    rule   = requests.get("http://example_rule_1:8001").content
    return 'Hello from User Service! \n %s \n %s' % (switch, rule)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)