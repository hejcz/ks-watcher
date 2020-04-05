# Kickstarter watcher

Project provides two scripts. `update.py` should be run as cron job. It updates `~/.ks_watcher/history.pickled` file and adds new kickstarter projects twohistory file.
The other script reads this file and opens browser with projects that you haven't seen yet.
