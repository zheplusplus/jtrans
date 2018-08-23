from datetime import datetime
import click

from . import __version__
from .route import find_route


def parse_date(_, __, date):
    if date is None:
        return datetime.now()
    return datetime.strptime(date, '%Y-%m-%d')


def parse_time(_, __, time):
    if time is None:
        return datetime.now()
    return datetime.strptime(time, '%H:%M')


@click.group()
def cli():
    pass


@cli.command(help='Find a route')
@click.argument('src', nargs=1, required=True)
@click.argument('dst', nargs=1, required=True)
@click.option('--date', callback=parse_date, help='Date. Today by default')
@click.option('--time', callback=parse_time, help='Time. Now by default')
def route(src, dst, date, time):
    find_route(src, dst, datetime.combine(date.date(), time.time()))


def main():
    cli()
