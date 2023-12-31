#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from crawler import asn
from crawler import geoip


def fetch(*impls) -> None:
    [x().fetch() for x in impls]


if __name__ == '__main__':
    fetch(asn.IPIP, asn.Fries, asn.BgpHe, asn.IPInfo, asn.BgpView, asn.DNSlytics)
    fetch(geoip.CZ88, geoip.IPIP, geoip.ChnRoute2, geoip.OperatorIP)
