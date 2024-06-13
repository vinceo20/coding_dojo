from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
app.secret_key = 'its a secret key, keep it safe'

@app.route('/user')
def index():

    users = User.get_all()

    return render_template('index.html', users = users)

# create
@app.route('/user/new')
def new_user():
    return render_template('/new.html')

@app.route('/user/create', methods = ['POST'])
def create_user():
    
    User.create(request.form)

    return redirect('/user')

# read
@app.route('/user/<int:id>')
def show_user(id):

    user = User.get_one(id)

    return render_template('show.html', user = user)

# update
@app.route('/user/edit/<int:user_id>')
def edit_user(user_id):

    user = User.get_one(user_id)

    return render_template('edit.html', user = user)

@app.route('/user/update', methods=['POST'])
def update_user():
    
    print(request.form)
    User.update(request.form)
    
    return redirect('/user')

# delete
@app.route('/user/delete/<int:id>')
def delete_user(id):
    User.delete(id)
    return redirect('/user')

if __name__=="__main__":
    app.run(debug=True)

