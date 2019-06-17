from flask import Flask, request, redirect
from shields import ShieldsColor, shields
from badge_status import get_badge_status

flask = Flask(__name__)
base_url = ""


@flask.route(base_url + "/")
def index():
    badge_url = shields("running", "OK", ShieldsColor.SUCCESS)
    return "<image src=\"" + badge_url + "\"/image>"


@flask.route(base_url + "/get_badge")
def get_badge():
    badge_id = request.args.get("id")
    if badge_id is None:
        badge_id = "xxxNOIDxxx"

    (label, message, color) = get_badge_status(badge_id)
    badge_url = shields(label, message, color)
    return redirect(badge_url)


if __name__ == '__main__':
    flask.run(port=16000, debug=True)