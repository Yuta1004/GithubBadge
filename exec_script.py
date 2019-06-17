import sqlite3
import subprocess
import os
import shutil


def get_script_name(badge_id):
    # Fetch DB
    connect = sqlite3.connect("badges.db")
    cur = connect.cursor()
    result = cur.execute("SELECT script FROM badge WHERE id = ?", (badge_id,))
    fetch_result = result.fetchall()
    cur.close()
    connect.close()

    script_name = fetch_result[0][0] if len(fetch_result) > 0 else -1
    return script_name


def clean_dir(path):
    # Listup dirs
    files = os.listdir(path)
    dir_list = [name for name in files if os.path.isdir(os.path.join(path, name))]

    for dir_name in dir_list:
        shutil.rmtree(os.path.join(path, dir_name))


def exec_script(badge_id):
    script_name = get_script_name(badge_id)
    if script_name == -1:
        return -1

    returncode = subprocess.run("cd scripts && ./" + script_name, shell=True).returncode
    clean_dir("./scripts")
    return returncode


if __name__ == "__main__":
    returncode = exec_script("badge")
    print(returncode)
