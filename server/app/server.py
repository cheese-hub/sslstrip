import flask
from flask import Flask, make_response, render_template, redirect, url_for, request 

#create the application object
app = Flask(__name__, template_folder='templates/')

#use decorators to link the function to a url
@app.route('/')
def home():
        return render_template("login.html")

@app.route('/welcome', methods=['GET','POST'])
def welcome():
        return render_template("welcome.html") #render a template

@app.route('/login', methods=['GET','POST'])
def login():
        error = None
        if request.method == 'POST':
                if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                        error = 'Invalid credentials. Please try again.'
                else:
                        #return redirect(url_for('welcome'))
                        return render_template("welcome.html")
        return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run()
