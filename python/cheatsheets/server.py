from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'its a secret key, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

