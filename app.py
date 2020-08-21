from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return "hello there!"


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid login credentials. please try again'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


# start the server with the run() method
if __name__ == '__main__':
    app.run(debug=True)