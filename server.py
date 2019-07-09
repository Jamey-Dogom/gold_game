from flask import Flask, redirect, request, render_template, session
import os
import random
import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if not session.get('msg'):
        session['msg'] = [] # needs to be a list
    if not session.get('gold'):
        session['gold'] = 0
    if not session.get('fontcolor'):
        session['fontcolor'] = "green"
    return render_template("index.html")

@app.route('/process-money', methods = ["POST"])
def process_money():
    user_guess = request.form['building']
    session['fontcolor'] = "green"
    
    if user_guess == 'farm':
        now = datetime.datetime.now()
        rand = random.randint(10, 20) 
        msg = "<p class = 'act' style = 'color: {}'>Earned {} golds from the {}! ({})<p>".format(session['fontcolor'],rand, user_guess, now.strftime("%Y-%m-%d %H:%M"))
        session['gold'] += rand
    if user_guess == 'cave':
        now = datetime.datetime.now()
        rand = random.randint(5, 10) 
        msg = "<p class = 'act' style = 'color: {}'>Earned {} golds from the {}! ({})<p>".format(session['fontcolor'],rand, user_guess, now.strftime("%Y-%m-%d %H:%M"))
        session['gold'] += rand
    if user_guess == 'house':
        now = datetime.datetime.now()
        rand = random.randint(2, 5) 
        msg = "<p class = 'act' style = 'color: {}'>Earned {} golds from the {}! ({})<p>".format(session['fontcolor'],rand, user_guess, now.strftime("%Y-%m-%d %H:%M"))
        session['gold'] += rand 
    if user_guess == 'casino':
        now = datetime.datetime.now()
        rand = random.randint(-50, 50) 
        if rand < 0:
            session['fontcolor'] = "red"
        msg = "<p class = 'act' style = 'color: {}'>Earned {} golds from the {}! ({})<p>".format(session['fontcolor'],rand, user_guess, now.strftime("%Y-%m-%d %H:%M"))
        session['gold'] += rand
        
        
    session['msg'].append(msg)

    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session['gold'] = 0
    session['msg'] = []

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

app.run(debug=True)