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
@click.option('--shinkansen/--no-shinkansen', default=True, help='Use Shinkansen or not')
@click.option('--limited-express/--no-limited-express', default=True, help='Use limited express or not')
@click.option('--show-all-stops/--no-show-all-stops', default=False,
              help='Show all stops (show only transfer stops and destination by default)')
def route(src, dst, date, time, **kwargs):
    find_route(src, dst, datetime.combine(date.date(), time.time()), kwargs)


def main():
    cli()
