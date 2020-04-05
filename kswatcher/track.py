import argparse
from history_file_support import load_history, save_history

parser = argparse.ArgumentParser(description='Track projects from Kickstarter.')
parser.add_argument('--add', type=int, nargs='+', help='add ids to tracking projects')
parser.add_argument('--remove', type=int, nargs='+', help='remove ids from tracking projects')

args = parser.parse_args()

history = load_history()

tracked = history["tracked"]

if args.remove is not None:
    tracked = tracked.difference(set(args.remove))

if args.add is not None:
    tracked = tracked.union(set(args.add))

history["tracked"] = tracked

save_history(history)
