from flask import Flask
from data import transform_daily_dialog

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == 'app':
    transform_daily_dialog()


if __name__ == '__main__':
    app.run()
