#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from .utils import Crawler
from typing import Generator


class Fries(Crawler):
    def __init__(self):
        super().__init__('Fries')
        self.__url = 'https://github.com/VirgilClyne/GetSomeFries/raw/main/ruleset/ASN.China.list'

    def fetch(self) -> None:
        raw = self._request(self.__url)
        self._dump([x for x in self.__parse(raw)])

    def __parse(self, raw: str) -> Generator[dict[str, int | str | bool], None, None]:
        for removed, asn, desc in self.__parse_raw(raw):
            yield {
                'asn': asn,
                'desc': desc.removesuffix('【未广播中国大陆IP】').strip(),
                'removed': removed,
                'inactive': desc.endswith('【未广播中国大陆IP】')
            }

    @staticmethod
    def __parse_raw(raw: str) -> Generator[tuple[bool, int, str], None, None]:
        for line in raw.splitlines():
            if line.startswith('IP-ASN'):
                if match := re.match(r'^IP-ASN, *(\d+) *//(.+)$', line):
                    yield True, int(match[1]), match[2].strip()
            elif line.startswith('# IP-ASN'):
                if match := re.match(r'^# *IP-ASN, *(\d+) *//(.+)$', line):
                    yield False, int(match[1]), match[2].strip()
