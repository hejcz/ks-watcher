# Kickstarter watcher

It allows you to track new projects on kickstarter.

## How to start

```bash
mkdir ~/.kswatcher
git clone https://github.com/hejcz/ks-watcher.git
cd ks-watcher
docker build -t kswatcher .
# add update to crontab e.g. */1 * * * * docker run --rm --volume ~/.kswatcher:/history kswatcher update
docker run --rm --volume ~/.kswatcher:/history kswatcher update
# check opens all new projects in your browser
docker run --rm --volume ~/.kswatcher:/history kswatcher check | xargs -r firefox
```
