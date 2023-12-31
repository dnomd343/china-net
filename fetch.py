#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from crawler import asn


def fetch(*impls) -> None:
    [x().fetch() for x in impls]


if __name__ == '__main__':
    fetch(asn.Fries, asn.BgpHe, asn.IPIP)
    # fetch(asn.IPInfo)
    # fetch(asn.DNSlytics)
