#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import netaddr
from ..utils import Crawler
from netaddr import IPNetwork


class ChnRoute2(Crawler):
    def __init__(self):
        super().__init__('chnroute2')

    def fetch(self) -> None:
        raw = self._request('https://github.com/misakaio/chnroutes2/raw/master/chnroutes.txt')
        self._dump(self.__parse_raw(raw))

    @staticmethod
    def __parse_raw(raw: str) -> list[str]:
        ips = [IPNetwork(x) for x in raw.splitlines() if not x.startswith('#')]
        return [str(x.cidr) for x in netaddr.cidr_merge(ips)]
