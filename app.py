from targets import targetsInfo
from flask import Flask, render_template
from polling import poll_host
app = Flask(__name__)

@app.route('/')
def index():
  for target in targetsInfo:
    status = poll_host(target["host"])
    target["status"] = status
  return render_template("index.html", targetsInfo=targetsInfo)

@app.route('/refresh')
def refresh():
  return render_template("index.html", targetsInfo=targetsInfo)

@app.route('/about')
def about():
  return render_template("about.html")


@app.route('/contact')
def contact():
  return render_template("contact.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)