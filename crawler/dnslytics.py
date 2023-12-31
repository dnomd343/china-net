#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from .utils import Crawler
from typing import Generator


class DNSlytics(Crawler):
    def __init__(self):
        super().__init__('DNSlytics')

    def fetch(self) -> None:
        raw = self._request('https://a.dnslytics.com/v1/report/asnhomepage', post={
            'q': 'cn',
            'dataset': 'asnhomepage',
        })
        self._dump([x for x in self.__parse_raw(raw)])

    @staticmethod
    def __parse_raw(raw: str) -> Generator[dict[str, int | str], None, None]:
        for info in json.loads(raw)['rootzone']:
            yield {
                'asn': info['asn'],
                'desc': info['shortname'],
                'date': info['rirdate'],
                'rank': info['rank'],
                'v4-prefix': info['nprefixv4'],
                'v6-prefix': info['nprefixv6'],
            }
