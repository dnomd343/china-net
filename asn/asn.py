#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .origin import AsnOrigin


class ASN:
    def __init__(self, asn: int):
        self.__asn = asn
        self.__desc = {}
        self.__v4_active = []
        self.__v6_active = []
        self.__v4_inactive = []
        self.__v6_inactive = []
        self.__rank = {}
        self.__v4_rank = {}
        self.__v6_rank = {}

    @property
    def desc(self) -> str:
        print(self.__desc)
        return ''

    @property
    def is_active(self) -> bool:
        print(
            [f'+{x.name}' for x in self.__v4_active],
            [f'-{x.name}' for x in self.__v4_inactive],
            [f'+{x.name}' for x in self.__v6_active],
            [f'-{x.name}' for x in self.__v6_inactive],
        )
        return True

    @property
    def rank(self) -> float:
        print(
            [f'{x.name} - {y}' for x, y in self.__rank.items()],
            [f'{x.name} - {y}' for x, y in self.__v4_rank.items()],
            [f'{x.name} - {y}' for x, y in self.__v6_rank.items()],
        )
        return 0

    def add_desc(self, origin: AsnOrigin, desc: str) -> None:
        desc = desc.strip()
        if desc != '':
            self.__desc[origin] = desc

    def mark_active(self, origin: AsnOrigin) -> None:
        self.mark_v4_active(origin)
        self.mark_v6_active(origin)

    def mark_inactive(self, origin: AsnOrigin) -> None:
        self.mark_v4_inactive(origin)
        self.mark_v6_inactive(origin)

    def mark_v4_active(self, origin: AsnOrigin) -> None:
        if origin not in self.__v4_active:
            self.__v4_active.append(origin)

    def mark_v6_active(self, origin: AsnOrigin) -> None:
        if origin not in self.__v6_active:
            self.__v6_active.append(origin)

    def mark_v4_inactive(self, origin: AsnOrigin) -> None:
        if origin not in self.__v4_inactive:
            self.__v4_inactive.append(origin)

    def mark_v6_inactive(self, origin: AsnOrigin) -> None:
        if origin not in self.__v6_inactive:
            self.__v6_inactive.append(origin)

    def add_rank(self, origin: AsnOrigin, rank: float) -> None:
        self.__rank[origin] = rank

    def add_v4_rank(self, origin: AsnOrigin, rank: float) -> None:
        self.__v4_rank[origin] = rank

    def add_v6_rank(self, origin: AsnOrigin, rank: float) -> None:
        self.__v6_rank[origin] = rank
