from flask import Flask
from flask import render_template
import relay_controller as relay
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('WebPage1.html')

@app.route('/on')
def on(name=None):
    relay.on(0)
    return "ok"

@app.route('/off')
def off():
    relay.off(0)
    return 'okej'

if __name__ == "__main__":
   try:
    relay.init()
    app.run(host= '0.0.0.0')
   finally:
    relay.off(0)
