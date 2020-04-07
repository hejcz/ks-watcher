import os
from history_file_support import load_history, save_history

last_history = load_history()

try:
    for project_id in last_history["tracked"]:
        p = last_history["project_by_id"][project_id]
        print("{} {} ({}%) - {}".format(p["id"], p["name"], p["success"], p["url"]))
    if len(last_history["new_ids"]) != 0:
        print(format("\n".join([last_history["project_by_id"][pid]["url"] for pid in last_history["new_ids"]])))
    last_history["new_ids"] = set()
    save_history(last_history)
except:
    print('error occured')
