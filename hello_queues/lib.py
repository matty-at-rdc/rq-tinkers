import requests
import time

from click import echo


def count_words_at_url_with_opts(url, sleep_time):
    resp = requests.get(url)
    count = len(resp.text.split())
    time.sleep(sleep_time)
    echo(
        f"\n=== Doing something cool now that I know that {url} contains {count} words ===\n"
    )
    return count
