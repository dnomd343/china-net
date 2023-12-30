#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .utils import Crawler
from typing import Generator
from bs4 import BeautifulSoup


class BgpHe(Crawler):
    def __init__(self):
        super().__init__('BgpHe')

    def fetch(self) -> None:
        raw = self._request('https://bgp.he.net/country/CN')
        self._dump([x for x in self.__parse(raw)])

    def __parse(self, raw: str) -> Generator[dict[str, int | str], None, None]:
        for info in self.__parse_raw(raw):
            yield {
                'asn': info[0],
                'desc': info[1],
                'v4-adjacency': info[2],
                'v4-route': info[3],
                'v6-adjacency': info[4],
                'v6-route': info[5],
            }

    @staticmethod
    def __parse_raw(raw: str) -> Generator[tuple[int, str, int, int, int, int], None, None]:
        body = BeautifulSoup(raw, 'lxml')
        table = body.find('table', id='asns').find('tbody')
        for row in table.find_all('tr'):
            info = [x.text for x in row.find_all('td')]
            asn = int(info[0].removeprefix('AS'))
            nums = [int(x.replace(',', '')) for x in info[2:6]]
            yield asn, info[1].strip(), *nums
