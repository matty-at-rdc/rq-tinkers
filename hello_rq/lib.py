import requests

def count_words_at_url(url):
    resp = requests.get(url)
    count = len(resp.text.split())
    print(f"Doing something cool now that I know that {url} contains {count} words...")
    return count 
