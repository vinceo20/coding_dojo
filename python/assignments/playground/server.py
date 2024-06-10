from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", times = 3, color = "blue")	# notice the 2 new named arguments!

@app.route('/play/<int:x>')
def play_x(x):
    return render_template("index.html", times = x, color = "blue")	# notice the 2 new named arguments!

@app.route('/play/<int:x>/<string:color>')
def play_x_color(x, color):
    return render_template("index.html", times = x, color = color)

if __name__=="__main__":
    app.run(debug=True)
