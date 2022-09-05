from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate')
def generate():
    return render_template('generate.html')


@app.route('/reference')
def reference():
    return render_template('reference.html')