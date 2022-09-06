from flask import Flask, render_template, request, url_for, redirect, g
import sqlite3
 
app = Flask(__name__)

MENUDB = 'dob.db'

@app.route('/', methods=['GET', 'POST'])
def index():
    db = sqlite3.connect(MENUDB)
    print(db)
    if request.method == 'POST':
        name = request.form["name"]
        return redirect(url_for('generate', name=name))
    return render_template('index.html')


@app.route('/generate', methods=['GET','POST'])
def generate():
    name = request.form.get('name')
    return render_template('generate.html', name=name)


@app.route('/reference', methods=['GET','POST'])
def reference():
    db = sqlite3.connect(MENUDB)
    print(db)
    
   
    return render_template('reference.html')

if __name__ == "__main__":
    app.run(debug=True)