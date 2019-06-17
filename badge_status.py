import sqlite3
from shields import ShieldsColor

def get_badge_status(badge_id):
    # Fetch DB
    connect = sqlite3.connect("badges.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM badge WHERE id = ?", (badge_id, ))
    fetch_result = cur.fetchall()
    cur.close()
    connect.close()

    if len(fetch_result) > 0:
        return fetch_result[0]
    else:
        return ("error", "badge not found",  ShieldsColor.CRITICAL.value)


if __name__ == '__main__':
    print(get_badge_status("test"))
    print(get_badge_status("badge"))
