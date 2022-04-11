from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/index')
def index():
    user = {'nutzername':'carl'}
    facts = [
        {
            'author': {'nutzername':'Lukas'},
            'left': 'Berlin',
            'rel': 'is the capital of',
            'right': 'Germany'
        },
        {
            'author': {'nutzername': 'Ingrid'},
            'left': 'Paris',
            'rel': 'is the capital of',
            'right': 'France'
        }
    ]
    return render_template('index.html', title='Home', user=user, facts=facts)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # When the browser sends the GET request to receive the web page with the form,
    # this method is going to return False. True is POST request i.e submit is clicked on login form
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template(url_for('login'), title='Sign In', form=form)
