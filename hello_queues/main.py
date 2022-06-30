import random
import time

from redis import Redis
from rq import Queue
from click import echo

from hello_queues.lib import count_words_at_url_with_opts

urls = [
    "https://google.com",
    "https://facebook.com",
    "https://linkedin.com",
    "https://hotels.com",
]

priorities = ["low", "medium", "high"]

sleep_times = [
    1.0,
    2.0,
    3.0,
]

timeouts = [
    "2s",
    "5s",
]


def random_from_list(_list):
    return random.choice(_list)


def main(url, priority, timeout, sleep_time):
    q = Queue(priority, connection=Redis())
    echo(
        f"Calling count_words_at_url with the following params: URL:{url}, Priority:{priority}, Timeout: {timeout}, Sleep Time: {sleep_time}...\n"
    )
    result = q.enqueue(
        count_words_at_url_with_opts,
        job_id=f"{priority}-{url}-{timeout}-{int(time.time())}",
        job_timeout=timeout,
        args=(
            url,
            sleep_time,
        ),
    )


def randomize(num):
    for i in range(num):
        url = random.choice(urls)
        priority = random.choice(priorities)
        sleep_time = random.choice(sleep_times)
        timeout = random.choice(timeouts)
        main(url, priority, timeout, sleep_time)
