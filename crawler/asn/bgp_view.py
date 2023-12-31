#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..utils import Crawler
from typing import Generator
from bs4 import BeautifulSoup


class BgpView(Crawler):
    def __init__(self):
        super().__init__('BgpView')

    def fetch(self) -> None:
        raw = self._request('https://bgpview.io/reports/countries/CN')
        self._dump([x for x in self.__parse(raw)])

    def __parse(self, raw: str) -> Generator[dict[str, int | str], None, None]:
        for asn, desc, nums, date in self.__parse_raw(raw):
            yield {
                'asn': asn,
                'desc': desc,
                'v4-prefix': nums[0],
                'v6-prefix': nums[1],
                'v4-peer': nums[2],
                'v6-peer': nums[3],
                'date': date,
            }

    @staticmethod
    def __parse_raw(raw: str) -> Generator[tuple[int, str, tuple[int, int, int, int], str], None, None]:
        table = BeautifulSoup(raw, 'lxml').find('table', id='country-report')
        for row in table.find('tbody').find_all('tr'):
            info = [x.text.strip() for x in row.find_all('td')]
            asn = int(info[0].removeprefix('AS'))
            nums = [int(x.replace(',', '')) for x in info[2:6]]
            yield asn, info[1], tuple(nums), info[-1]
