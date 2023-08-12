from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test_add.html')

@app.route('/add_numbers', methods=['POST'])
def add_numbers():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 + num2
    return f"The sum of your two numbers is: {result}"

if __name__ == '__main__':
    app.run(debug=True)
