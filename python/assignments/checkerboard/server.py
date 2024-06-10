from flask import Flask, render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    return render_template("index.html", row = 8, col = 8, col_1 = "red", col_2 = "blue")

@app.route('/<int:x>')
def index_x(x):
    return render_template("index.html", row = x, col = 8, col_1 = "red", col_2 = "blue")

@app.route('/<int:x>/<int:y>')
def index_x_y(x,y):
    return render_template("index.html", row = x, col = y, col_1 = "red", col_2 = "blue")

@app.route('/<int:x>/<int:y>/<string:col_1>')
def index_x_y_col1(x,y,col_1):
    return render_template("index.html", row = x, col = y, col_1 = col_1, col_2 = "blue")

@app.route('/<int:x>/<int:y>/<string:col_1>/<string:col_2>')
def index_x_y_col1_col2(x,y,col_1,col_2):
    return render_template("index.html", row = x, col = y, col_1 = col_1, col_2 = col_2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.