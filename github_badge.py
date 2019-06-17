from flask import Flask, request, redirect
from shields import ShieldsColor, shields
from badge_status import get_badge_status, update_badge_status
from exec_script import exec_script

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


@flask.route(base_url + "/webhook/<badge_id>", methods=["GET", "POST"])
def webhook(badge_id):
    returncode = exec_script(badge_id)
    update_result = update_badge_status(badge_id, returncode)
    return str(update_result)


if __name__ == '__main__':
    flask.run(port=16000, debug=True)
