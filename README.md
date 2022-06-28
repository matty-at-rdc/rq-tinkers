# RQ Tinkers

## What is this?

This is a cool repo that will help you play around with RQ on your local machine.

## Pre-Reqs

- Run Redis in a Container

```sh
docker run --name rq-redis -p 6379:6379 -d redis
# docker ps # fine your redis server working...
```