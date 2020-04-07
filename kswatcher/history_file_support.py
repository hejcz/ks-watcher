import os.path
import pickle

ks_path = '/history/history.pickled'

def load_history():
    last_history = None
    try:
        with open(ks_path, 'rb') as f:
            last_history = pickle.load(f)
    except IOError:
        pass

    if last_history is None:
        last_history = {}
    
    if "all_ids" not in last_history:
        last_history["all_ids"] = set()
    
    if "new_ids" not in last_history:
        last_history["new_ids"] = set()

    if "project_by_id" not in last_history:
        last_history["project_by_id"] = {}

    if "tracked" not in last_history:
        last_history["tracked"] = set()

    return last_history

def save_history(history):
    pickle.dump(history, open(ks_path, 'wb+'))
