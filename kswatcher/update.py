# goal of this script is to:
# - track new popular kickstarter projects
# - inform me about new projects
# - allow me to check new projects (the ones I haven't seen yet) with a single command and provide links

import json
from datetime import datetime
from history_file_support import load_history, save_history

import requests

last_history = load_history()

new_history = {"all_ids": set(), "new_ids": set(), "project_by_id": last_history["project_by_id"], "tracked": last_history["tracked"]}

pages_to_fetch = 3

current_ids = []
for page in range(1, pages_to_fetch + 1):
    response = requests.get('https://www.kickstarter.com/discover/advanced', 
        params={"category_id": 34, "sort": "popularity", "page": page},
        headers={"Accept": "application/json"})
    projects = json.loads(response.text)
    new_history["project_by_id"].update({p["id"]:{"id": p["id"], "name": p["name"], "url": p["urls"]["web"]["project"], \
        "success": "{:.2f}".format(100 * int(p["pledged"]) / int(p["goal"])), "currency": p["currency"], "goal": p["goal"], "pledged": p["pledged"], "backers_count": p["backers_count"]} for p in projects["projects"]})
    current_ids = current_ids + [p["id"] for p in projects["projects"]]

new_history["last_update"] = datetime.now()

new_projects = set(current_ids).difference(last_history["all_ids"])

new_history["all_ids"] = last_history["all_ids"].union(new_projects)
new_history["new_ids"] = last_history["new_ids"].union(new_projects)

save_history(new_history)
