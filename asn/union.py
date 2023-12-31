#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import math
from .asn import ASN
from logger import logger
from .origin import AsnOrigin


class AsnUnion:
    def __init__(self):
        self.__asns = {}
        self.__apply_ipip()
        self.__apply_fries()
        self.__apply_bgp_he()
        self.__apply_ipinfo()
        self.__apply_bgp_view()
        self.__apply_dnslytics()

    def export(self) -> list[ASN]:
        """ Export all loaded ASN object. """
        return list(self.__asns.values())

    def __get_asn(self, asn: int) -> ASN:
        """ Get ASN object with its number. """
        return self.__asns[asn]

    def __init_asns(self, asns: list[int]) -> None:
        """ Batch initialization ASN object. """
        asns = [x for x in asns if x not in self.__asns]  # filter non-init ASNs
        self.__asns |= {x: ASN(x) for x in asns}

    def __apply_ipip(self) -> None:
        """ Apply ASN upstream data of *IPIP*. """
        origin = AsnOrigin.IPIP
        data = self.__load_data(origin)
        v4_max = math.log2(max([x['v4-num'] for x in data.values()]))
        v6_max = math.log2(max([x['v6-num'] for x in data.values()]))

        for asn, info in data.items():
            asn = self.__get_asn(asn)
            asn.add_desc(origin, info['desc'])
            v4_num, v6_num = info['v4-num'], info['v6-num']

            if v4_num == 0:
                asn.mark_v4_inactive(origin)
                asn.add_v4_rank(origin, 0)
            else:
                asn.mark_v4_active(origin)
                asn.add_v4_rank(origin, math.log2(v4_num) / v4_max)

            if v6_num == 0:
                asn.mark_v6_inactive(origin)
                asn.add_v6_rank(origin, 0)
            else:
                asn.mark_v6_active(origin)
                asn.add_v6_rank(origin, math.log2(v6_num) / v6_max)

    def __apply_fries(self) -> None:
        """ Apply ASN upstream data of *Fries*. """
        origin = AsnOrigin.Fries
        for asn, info in self.__load_data(origin).items():
            asn = self.__get_asn(asn)
            asn.add_desc(origin, info['desc'])
            if info['removed'] or info['inactive']:
                asn.mark_inactive(origin)
            else:
                asn.mark_active(origin)

    def __apply_bgp_he(self) -> None:
        """ Apply ASN upstream data of *BgpHe*. """
        origin = AsnOrigin.BgpHe
        for asn, info in self.__load_data(origin).items():
            asn = self.__get_asn(asn)
            asn.add_desc(origin, info['desc'])

            if info['v4-adjacency'] == 0 or info['v4-route'] == 0:
                asn.mark_v4_inactive(origin)
            else:
                asn.mark_v4_active(origin)

            if info['v6-adjacency'] == 0 or info['v6-route'] == 0:
                asn.mark_v6_inactive(origin)
            else:
                asn.mark_v6_active(origin)

    def __apply_ipinfo(self) -> None:
        """ Apply ASN upstream data of *IPInfo*. """
        origin = AsnOrigin.IPInfo
        data = self.__load_data(origin)
        max_rank = math.log2(max([x['num'] for x in data.values()]))
        for asn, info in data.items():
            asn = self.__get_asn(asn)
            asn.add_desc(origin, info['desc'])
            if info['type'] == 'inactive' or info['num'] == 0:
                asn.mark_inactive(origin)
                asn.add_rank(origin, 0)
            else:
                asn.mark_active(origin)
                asn.add_rank(origin, math.log2(info['num']) / max_rank)

    def __apply_bgp_view(self) -> None:
        """ Apply ASN upstream data of *BgpView*. """
        origin = AsnOrigin.BgpView
        for asn, info in self.__load_data(origin).items():
            asn = self.__get_asn(asn)
            asn.add_desc(origin, info['desc'])

            if info['v4-prefix'] == 0 or info['v4-peer'] == 0:
                asn.mark_v4_inactive(origin)
            else:
                asn.mark_v4_active(origin)

            if info['v6-prefix'] == 0 or info['v6-peer'] == 0:
                asn.mark_v6_inactive(origin)
            else:
                asn.mark_v6_active(origin)

    def __apply_dnslytics(self) -> None:
        """ Apply ASN upstream data of *DNSlytics*. """
        origin = AsnOrigin.DNSlytics
        data = self.__load_data(origin)
        for asn, info in data.items():
            asn = self.__get_asn(asn)
            asn.add_desc(origin, info['desc'])

            if info['v4-prefix'] == 0:
                asn.mark_v4_inactive(origin)
            else:
                asn.mark_v4_active(origin)

            if info['v6-prefix'] == 0:
                asn.mark_v6_inactive(origin)
            else:
                asn.mark_v6_active(origin)

    def __load_data(self, origin: AsnOrigin) -> dict[int, dict[str, int | str | bool]]:
        """ Load ASN upstream raw data from JSON file. """
        raw = open(f'release/raw/{origin.name}.json').read()
        data = {info.pop('asn'): info for info in json.loads(raw)}
        logger.info(f'ASN data upstream `{origin.name}` -> {len(data)} items')
        self.__init_asns(list(data))
        return data
