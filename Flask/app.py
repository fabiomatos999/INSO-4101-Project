#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request, flash
#from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'bdbsahdbhasbdsab hsbdhasbdhbashdbas'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@app.route('/logout')
def logout():
    return "<p>logout</p>"

@app.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('email')
        password = request.form.get('pwd')
        confirmPassword = request.form.get('confirm-pwd')

        if(len(email) < 4):
            flash("Email must be greater than 4 characters", category='error')
        elif len(username) < 4:
            flash("Username must be greater than 4 characters", category='error')
        elif password != confirmPassword:
            flash("Password doesnt match with confirm password", category='error')
        elif len(password) < 7:
            flash("Password must be greater than 7 characters", category='error')
        else:
            #add user to the database
            flash("Account created succesfully!", category='success')
            
    
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
