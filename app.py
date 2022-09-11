from sqlite3 import dbapi2
from flask import Flask, render_template, request, url_for, redirect, g
import sqlite3
 
app = Flask(__name__)

MENUDB = 'dob.db'

@app.route('/', methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
        name = request.form["name"]
        return redirect(url_for('generate', name=name)) # Is name=name needed here?
     return render_template('index.html')

# request function for image category input.
@app.route('/generate', methods=['GET','POST'])
def generate():
    if request.method == 'POST':
       imgcate = request.form['']
       return redirect(url_for('reference'))

    name = request.form.get('name')
    return render_template('generate.html', name=name)
    


#import db for poem section,
#import db for image section, blob selection based on category input above.
@app.route('/reference', methods=['GET','POST'])
def reference():
    db = sqlite3.connect(MENUDB)
    print(db)
    
   
    return render_template('reference.html')

if __name__ == "__main__":
    app.run(debug=True)