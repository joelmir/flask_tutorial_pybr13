from flask import Flask

app = Flask(__name__)
app.config['FOO'] = 'BAR'
app.config['DEBUG'] = True


@app.route('/hello')
def hello():
    return 'Hello'


if __name__ == '__main__':
    app.run(use_reloader=True)