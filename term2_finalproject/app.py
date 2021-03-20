from flask import flask, render_template, current_app as current_app
from sense hat import SenseHat
app = Flask (__name__)

@app.route('/log_in')
def log_in()
return render_template('log_in.html')

@app.route('/success', methods=['GET', 'POST'])
def success()



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')