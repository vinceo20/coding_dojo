from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'its a secret key, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_number():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    
    guess_number = int(request.form('number'))
    return redirect('/', guess_number=guess_number)

if __name__=="__main__":
    app.run(debug=True)

