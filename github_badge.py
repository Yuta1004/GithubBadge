from flask import Flask

flask = Flask(__name__)


@flask.route("/")
def index():
    return "Github Badge"


if __name__ == '__main__':
    flask.run(port=16000, debug=True)