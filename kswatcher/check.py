import json
import os
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
    last_history = {"all_ids": set(), "new_ids": [], "project_by_id": {}}

if len(last_history["new_ids"]) != 0:
    os.system("firefox {0}".format(" ".join([last_history["project_by_id"][pid]["url"] for pid in last_history["new_ids"]])))

last_history["new_ids"] = set()

pickle.dump(last_history, open(ks_path, 'wb+'))
