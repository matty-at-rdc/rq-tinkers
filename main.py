import click

from hello_rq.main import main as hello_rq_main

@click.command
@click.option("--url", default="https://google.com", help="The url to send to the word counter...")
def hello_rq_cmd(url):
    hello_rq_main(url)


if __name__ == "__main__":
    hello_rq_cmd()