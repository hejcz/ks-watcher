# goal of this script is to:
# - track new popular kickstarter projects
# - inform me about new projects
# - allow me to check new projects (the ones I haven't seen yet) with a single command and provide links

import json
import os.path
import pickle
from datetime import datetime

import requests

ks_path = os.path.expanduser("~") + '/.ks_watcher/history.pickled'
last_history = None
try:
    with open(ks_path, 'rb') as f:
        last_history = pickle.load(f)
except IOError:
    pass

if last_history is None:
    last_history = {"all_ids": set(), "new_ids": set(), "project_by_id": {}}

new_history = {"all_ids": set(), "new_ids": set(), "project_by_id": last_history["project_by_id"]}

pages_to_fetch = 3

current_ids = []
for page in range(1, pages_to_fetch + 1):
    response = requests.get('https://www.kickstarter.com/discover/advanced', 
        params={"category_id": 34, "sort": "popularity", "page": page},
        headers={"Accept": "application/json"})
    projects = json.loads(response.text)
    new_history["project_by_id"].update({p["id"]:{"url": p["urls"]["web"]["project"], "name": p["name"]} for p in projects["projects"]})
    current_ids = current_ids + [p["id"] for p in projects["projects"]]

new_history["last_update"] = datetime.now()

new_projects = set(current_ids).difference(last_history["all_ids"])

new_history["all_ids"] = last_history["all_ids"].union(new_projects)
new_history["new_ids"] = last_history["new_ids"].union(new_projects)

pickle.dump(new_history, open(ks_path, 'wb+'))
