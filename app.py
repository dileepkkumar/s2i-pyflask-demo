from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World ! - Pygjhgchchjco</h1>'

@app.route('/version')
def get_version():
    return '<h1>App version : <b>44.5</b></h1>'

@app.route('/test')
def get_test():
    return '<h1>You are accessing /tmvdmvhjsbvs</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
