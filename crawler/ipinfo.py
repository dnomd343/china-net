#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from .utils import Crawler
from typing import Generator


class IPInfo(Crawler):
    def __init__(self):
        super().__init__('IPInfo')

    def fetch(self) -> None:
        url = 'https://ipinfo.io/api/data/asns?country=cn'
        self._dump([x for items in self.__fetch(url) for x in items])

    def __fetch(self, url: str) -> Generator[list[dict], None, None]:
        page_num = 0
        while True:
            raw = self._request(f'{url}&amount=20&page={page_num}')
            items = [x for x in self.__parse_raw(raw)]
            if len(items) == 0:
                break
            page_num += 1
            yield items

    @staticmethod
    def __parse_raw(raw: str) -> Generator[dict[str, int | str], None, None]:
        for info in json.loads(raw):
            yield {
                'asn': int(info['asn'].removeprefix('AS')),
                'desc': info['name'].strip(),
                'num': info['numberOfIps'],
                'type': info['type'],
            }
