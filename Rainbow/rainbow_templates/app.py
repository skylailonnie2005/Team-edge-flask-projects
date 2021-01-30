from flask import Flask, render_template, current_app as current_app

app = Flask (_name_)

@app.route('/')
def index():
    return ....











if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
