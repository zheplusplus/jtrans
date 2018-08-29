import re
import requests
from lxml.html import HtmlComment
from pyquery import PyQuery as q


_INT = re.compile(r'(\d|,)+')


def _parse_fare(f):
    m = _INT.search(f)
    if m is None:
        return ' -'
    return ' =Y= {}'.format(m.group(0))


def _no_comment(i):
    for o in i:
        if isinstance(o, HtmlComment):
            continue
        yield q(o)


class RouteDisplay:
    def __init__(self, options):
        if not options['show_all_stops']:
            self._format_stops = lambda _: None

    def format_root(self, root):
        for dtl in root('.routeDetail'):
            print('=' * 80)
            for item in _no_comment(dtl):
                self._format_item(item)

    def _format_item(self, item):
        cls = item.attr('class')
        if cls == 'station':
            self._format_station(item)
        elif cls == 'fareSection':
            self._format_fare_sec(item)
        elif cls == 'fareSection express':
            self._format_fare_exp(item)
        elif cls == 'fare':
            self._format_fare(item)
        elif cls == 'access':
            self._format_access(item)
        elif cls == 'access walk':
            self._format_walk(item)
        else:
            print('       X-> ', item.attr('class'), 'Please report this message')

    def _format_station(self, sta):
        print(sta('dl dt').text())
        print('  ', sta('.time li').text())

    def _format_fare_sec(self, fare_sta):
        for item in _no_comment(fare_sta.children()):
            self._format_item(item)

    def _format_fare_exp(self, fare_sta):
        for item in _no_comment(fare_sta.children()):
            if item.attr('class') == 'fare':
                print(_parse_fare(item.text()), 'for limited express')
                continue
            self._format_item(item)


    def _format_fare(self, fare):
        print(_parse_fare(fare.text()))

    def _format_stops(self, acc):
        for stop in _no_comment(acc('.stop dl')):
            print('    ', stop('dt').text(), stop('dd').text())

    def _format_access(self, acc):
        print('  ', acc('.transport div').text())

        platform_text = acc('.platform').text()
        if platform_text:
            print('  ', platform_text)

        stop_num = acc('.btnStopNum').text()
        if stop_num:
            print('    ', stop_num)
        self._format_stops(acc)

    def _format_walk(self, w):
        print('... Walk ...')


def find_route(src, dst, dt, options):
    def _opt_to_char(opt):
        return '1' if options[opt] else '0'

    head_info = '{} ==> {} at {}'.format(src, dst, dt.strftime('%Y-%m-%d %H:%M'))
    print(head_info)
    dt_str = dt.strftime('%Y%m%d%H%M')
    root = q(str(requests.get(
        'https://transit.yahoo.co.jp/search/result',
        params={
            'flatlon': '',
            'from': src,
            'tlatlon': '',
            'to': dst,
            'viacode': '',
            'via': '',
            'y': dt_str[:4],
            'm': dt_str[4:6],
            'd': dt_str[6:8],
            'hh': dt_str[8:10],
            'm1': dt_str[10:11],
            'm2': dt_str[11:12],
            'ticket': 'ic',
            'expkind': '1',
            'ws': '3',
            's': '0',
            'al': '1',
            'shin': _opt_to_char('shinkansen'),
            'ex': _opt_to_char('limited_express'),
            'hb': '1',
            'lb': '1',
            'sr': '1',
            'kw': '',
        }).content, 'utf-8'))

    RouteDisplay(options).format_root(root)

    print('=' * 80)
    print(head_info)
