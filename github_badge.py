from flask import Flask
from shields import ShieldsColor, shields

flask = Flask(__name__)


@flask.route("/")
def index():
    badge_url = shields("running", "OK", ShieldsColor.SUCCESS)
    return "<image src=\"" + badge_url + "\"/image>"


if __name__ == '__main__':
    flask.run(port=16000, debug=True)