#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .origin import AsnOrigin


class ASN:
    def __init__(self, asn: int):
        self.__asn = asn

    def add_desc(self, origin: AsnOrigin, desc: str) -> None:
        # print(self.__asn, origin, desc)
        pass

    def mark_inactive(self, origin: AsnOrigin) -> None:
        # print(self.__asn)
        pass

    def mark_v4_inactive(self, origin: AsnOrigin) -> None:
        # print(self.__asn)
        pass

    def mark_v6_inactive(self, origin: AsnOrigin) -> None:
        # print(self.__asn)
        pass

    def add_rank(self, origin: AsnOrigin, rank: float) -> None:
        # print(self.__asn, rank)
        pass

    def add_v4_rank(self, origin: AsnOrigin, rank: float) -> None:
        # print(self.__asn, rank)
        pass

    def add_v6_rank(self, origin: AsnOrigin, rank: float) -> None:
        # print(self.__asn, rank)
        pass
