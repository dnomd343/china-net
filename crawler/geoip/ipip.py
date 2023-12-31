#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import netaddr
from ..utils import Crawler
from netaddr import IPNetwork


class IPIP(Crawler):
    def __init__(self):
        super().__init__('17mon')

    def fetch(self) -> None:
        raw = self._request('https://github.com/17mon/china_ip_list/raw/master/china_ip_list.txt')
        self._dump(self.__parse_raw(raw))

    @staticmethod
    def __parse_raw(raw: str) -> list[str]:
        ips = [IPNetwork(x) for x in raw.splitlines()]
        return [str(x.cidr) for x in netaddr.cidr_merge(ips)]
