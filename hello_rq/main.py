from redis import Redis
from rq import Queue

from hello_rq.lib import count_words_at_url

def main(url):
    q = Queue(connection=Redis())
    result = q.enqueue(count_words_at_url, url)
