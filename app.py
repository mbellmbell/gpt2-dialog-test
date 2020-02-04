from flask import Flask
from format_dailydialog import transform_daily_dialog

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
