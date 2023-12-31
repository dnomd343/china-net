#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from crawler import asn
from crawler import geoip


def fetch(*impls) -> None:
    [x().fetch() for x in impls]


if __name__ == '__main__':
    fetch(asn.Fries, asn.BgpHe, asn.IPIP, asn.IPInfo, asn.DNSlytics)
    fetch(geoip.IPIP, geoip.CZ88, geoip.ChnRoute2, geoip.OperatorIP)
