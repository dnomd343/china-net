#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .origin import AsnOrigin


class ASN:
    def __init__(self, asn: int):
        self.__asn = asn
        self.__desc = {}

        self.__active = []
        self.__v4_active = []
        self.__v6_active = []
        self.__v4_inactive = []
        self.__v6_inactive = []

        self.__rank = {}
        self.__v4_rank = {}
        self.__v6_rank = {}

    @property
    def asn(self) -> int:
        return self.__asn

    @property
    def desc(self) -> str:
        if len(self.__desc) == 0:  # unknown description
            return ''
        names = sorted({x.removesuffix(', CN') for x in self.__desc.values()})

        for name in names[::1]:
            for other in [x for x in names if x != name]:
                if name.lower() in other.lower():
                    names.remove(name)
                    break  # only remove once
        if len(names) == 1:
            return names[0]

        print(names)

        return ''

    @property
    def v4_active(self) -> bool:
        if len(self.__v4_active) > 0:  # tend to be active
            return True
        if set(self.__v4_inactive) == set(self.__v6_active):  # more likely only ipv6
            return False
        if len(self.__active) == 0 and len(self.__v4_inactive) > 0:  # no one considers active
            return False
        if len(self.__v6_active) > 0 and set(self.__v6_active) - set(self.__v4_inactive) == set():  # seems ipv6 only
            return False
        return len(self.__v4_inactive) == 0

    @property
    def v6_active(self) -> bool:
        if len(self.__v6_active) > 0:  # tend to be active
            return True
        if len(self.__active) == 0 and set(self.__v4_inactive) == set(self.__v6_inactive):  # more likely both inactive
            return False
        if len(self.__active) == 0 and len(self.__v6_inactive) > 0:  # no one considers active
            return False
        if len(self.__active) > 0 and set(self.__v4_active) == set(self.__v6_inactive):  # more likely only ipv4
            return False
        if len(self.__v4_active) > 0 and set(self.__v4_active) - set(self.__v6_inactive) == set():  # seems ipv4 only
            return False
        return len(self.__active) != 0

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
        self.__active.append(origin)

    def mark_inactive(self, origin: AsnOrigin) -> None:
        self.mark_v4_inactive(origin)
        self.mark_v6_inactive(origin)

    def mark_v4_active(self, origin: AsnOrigin) -> None:
        self.__v4_active.append(origin)

    def mark_v6_active(self, origin: AsnOrigin) -> None:
        self.__v6_active.append(origin)

    def mark_v4_inactive(self, origin: AsnOrigin) -> None:
        self.__v4_inactive.append(origin)

    def mark_v6_inactive(self, origin: AsnOrigin) -> None:
        self.__v6_inactive.append(origin)

    def add_rank(self, origin: AsnOrigin, rank: float) -> None:
        self.__rank[origin] = rank

    def add_v4_rank(self, origin: AsnOrigin, rank: float) -> None:
        self.__v4_rank[origin] = rank

    def add_v6_rank(self, origin: AsnOrigin, rank: float) -> None:
        self.__v6_rank[origin] = rank
