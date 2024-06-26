from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'its a secret key, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count')
def count():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

