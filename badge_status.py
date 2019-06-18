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
        return fetch_result[0][1:4]
    else:
        return ("error", "badge not found",  ShieldsColor.CRITICAL.value)


def update_badge_status(badge_id, status):
    connect = sqlite3.connect("badges.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM badge WHERE id = ?", (badge_id, ))
    if len(cur.fetchall()) == 0:
        return -1

    message = "ok" if status == 0 else "failed"
    color = "success" if status == 0 else "important"
    cur.execute("UPDATE badge SET message = ?, color = ? WHERE id = ?", (message, color, badge_id))
    connect.commit()
    cur.close()
    connect.close()
    return 0


if __name__ == '__main__':
    print(get_badge_status("test"))
    print(get_badge_status("badge"))
    print(update_badge_status("test", 0))
    print(update_badge_status("badge", 0))
    print(get_badge_status("badge"))
