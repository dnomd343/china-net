#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from .asn import ASN


class AsnUnion:
    def __init__(self):
        self.__asns: dict[int, ASN] = {}

        self.__apply_ipip()
        self.__apply_fries()
        self.__apply_bgp_he()
        self.__apply_ipinfo()
        self.__apply_dnslytics()

    def __init_asns(self, asns: list[int]) -> None:
        asns = [x for x in asns if x not in self.__asns]  # filter non-init ASNs
        self.__asns |= {x: ASN(x) for x in asns}

    def __apply_ipip(self) -> None:
        data = self.__load_data('IPIP')
        print(len(self.__asns))

    def __apply_fries(self) -> None:
        data = self.__load_data('Fries')
        print(len(self.__asns))

    def __apply_bgp_he(self) -> None:
        data = self.__load_data('BgpHe')
        print(len(self.__asns))

    def __apply_ipinfo(self) -> None:
        data = self.__load_data('IPInfo')
        print(len(self.__asns))

    def __apply_dnslytics(self) -> None:
        data = self.__load_data('DNSlytics')
        print(len(self.__asns))

    def __load_data(self, tag: str) -> dict[int, dict[str, int | str | bool]]:
        raw = open(f'release/raw/{tag}.json').read()
        data = {info.pop('asn'): info for info in json.loads(raw)}
        self.__init_asns(list(data))
        return data
