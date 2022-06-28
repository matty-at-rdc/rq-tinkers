# RQ Tinkers 🍤

## What is this?

This is a cool repo 😎 that will help you play around with RQ on your local machine.

## Pre-Reqs

- Have Python3 On Your Machine

```sh
python3 --version
```

- Run Redis in a Container (means you also need Docker I suppose)

```sh
docker run --name rq-redis -p 6379:6379 -d redis
# docker ps # fine your redis server working...
```

## Set Up

- Clone/Download/Fork this repository

```sh
git clone git@github.com:matty-at-rdc/rq-tinkers.git
```

- Create and activate a Virtual Env

```sh
python3 -m venv .venv && source .venv/bin/activate
```

- Install dependencies

```sh
pip install --requirement requirements.txt
```

- Start an RQ Worker (this process owns this terminal instance now)

```sh
rq worker --with-scheduler 
# OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES rq worker --with-scheduler # On Mac
# See: https://hynek.me/til/rq-macos/
```

- Run a lesson / module using _main/py_ (in future you can use `--help` to see more examples)

```sh
python main.py 
```

- Observe the worker accomplishing your dreams in the worker process

```sh
# 16:50:11 default: hello_rq.lib.count_words_at_url('https://google.com') (e5159866-c572-4833-a3b5-3c280b29bcc7)
# Doing something cool now that I know that https://google.com contains 396 words...
# 16:50:12 default: Job OK (e5159866-c572-4833-a3b5-3c280b29bcc7)
```