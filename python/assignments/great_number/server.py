from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'its a secret key, keep it safe'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,100)

    if 'attempt' not in session:
        session['attempt'] = 0
    
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess_your_number():
    
    if request.form['guess_number']:
        guess_number = int(request.form['guess_number'])
        session['guess_number'] = guess_number
    
    print(session['number'])

    if 'attempt' not in session:
        session['attempt'] = 0
    
    session['attempt'] += 1
    
    print(session['attempt'])

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

