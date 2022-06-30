import click

from hello_rq.main import main as hello_rq_main
from hello_queues.main import (
    main as hello_queues_main,
    randomize as hello_queues_randomize,
)


@click.group()
def cmds():
    pass


@click.command
@click.option(
    "--url", default="https://google.com", help="The url to send to the word counter"
)
def hello_rq_cmd(url):
    hello_rq_main(url)


@click.command
@click.option(
    "--url", default="https://google.com", help="The url to send to the word counter"
)
@click.option(
    "--priority",
    default="medium",
    help="The queue/prioirty of the job in question. Simulates high and low priority jobs.",
)
@click.option(
    "--timeout",
    default="25s",
    help="The amount of time RQ should wait before failing the job for taking too long",
)
@click.option(
    "--sleep-time",
    default=0,
    help="The amount of time the functions should wait befor executing. This simulates lag.",
)
def hello_queues_cmd(url, priority, timeout, sleep_time):
    hello_queues_main(url, priority, timeout, sleep_time)


@click.command
@click.option(
    "--num",
    type=int,
    default=5,
    help="The number of times to requests rq do randoms things",
)
def hello_queues_random_cmd(num):
    hello_queues_randomize(num)


cmds.add_command(hello_rq_cmd)
cmds.add_command(hello_queues_cmd)
cmds.add_command(hello_queues_random_cmd)


if __name__ == "__main__":
    cmds()
