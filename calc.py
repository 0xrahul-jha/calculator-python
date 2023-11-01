from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['first_number'])
    b = float(request.form['second_number'])
    result = a + b

    if result.is_integer():
        result = int(result)

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
