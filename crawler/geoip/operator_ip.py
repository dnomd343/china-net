#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import netaddr
from ..utils import Crawler
from netaddr import IPNetwork


class OperatorIP(Crawler):
    def __init__(self):
        super().__init__('china-operator-ip')

    def fetch(self) -> None:
        tags = ['cernet', 'china', 'chinanet', 'cmcc', 'cstnet','drpeng', 'googlecn', 'tietong', 'unicom']
        tags += [f'{x}6' for x in tags]
        urls = [f'https://gaoyifan.github.io/china-operator-ip/{x}.txt' for x in tags]
        raw = '\n'.join([self._request(x) for x in urls])
        self._dump(self.__parse_raw(raw))

    @staticmethod
    def __parse_raw(raw: str) -> list[str]:
        ips = [IPNetwork(x) for x in raw.splitlines() if x != '']
        return [str(x.cidr) for x in netaddr.cidr_merge(ips)]
