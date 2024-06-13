from flask import Flask, render_template, request, redirect, session
from user import User

app = Flask(__name__)
app.secret_key = 'its a secret key, keep it safe'

@app.route('/')
def index():

    users = User.get_all()
    print(users)

    return render_template('index.html', users = users)

@app.route('/new')
def create_new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
