#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .utils import Crawler
from typing import Generator
from bs4 import BeautifulSoup


class IPIP(Crawler):
    def __init__(self):
        super().__init__('IPIP')

    def fetch(self) -> None:
        raw = self._request('https://whois.ipip.net/iso/CN')
        self._dump([x for x in self.__parse(raw)])

    def __parse(self, raw: str) -> Generator[dict[str, int | str], None, None]:
        for info in self.__parse_raw(raw):
            yield {
                'asn': info[0],
                'desc': info[1],
                'v4-num': info[2],
                'v6-num': info[3],
            }

    @staticmethod
    def __parse_raw(raw: str) -> Generator[tuple[int, str, int, int], None, None]:
        table = BeautifulSoup(raw, 'lxml').find('table')
        table.find('thead').clear()
        for row in table.find_all('tr'):
            info = [x.text for x in row.find_all('td')]
            asn = int(info[0].removeprefix('AS'))
            to_int = lambda x: int(x.replace(',', ''))
            yield asn, info[1].strip(), to_int(info[2]), to_int(info[3])
