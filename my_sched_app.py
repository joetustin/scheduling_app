from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/edit")
def edit():
    return render_template('sch_ed.html')

@app.route("/schedule")
def schedule():
    return render_template('schedule.html')

@app.route("/admin", methods=['GET', 'POST'])
def login():
    error=None;
    if request.method =='POST':
        if request.form['username'] != 'joe@nylas.com' or request.form['password'] != 'Joe,T!12':
            error = 'Invalid credentials. Please try again.';
        else:
            return redirect(url_for('edit'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
