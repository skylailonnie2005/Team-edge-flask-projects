from flask import Flask, render_template, current_app as current_app

app = Flask (_name_)

@app.route('/')
def index():
    return ....

@app.route('/red')
def red():
    return render_template('red.html')

@app.route('/orange')
def orange():
    return render_template('orange.html')

@app.route('/yellow')
def yellow():
    return render_template('yellow.html')

@app.route('/green')
def green():
    return render_template('green.html')

@app.route('/blue')
def blue():
    return render_template('blue.html')

@app.route('/indigo')
def indigo():
    return render_template('indigo.html')

@app.route('/violet')
def violet():
    return render_template('indigo.html')

@app.route('/rainbow')
def rainbow();
    return render_template('rainbow.html')









if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
