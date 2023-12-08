#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import netaddr

from netaddr import IPNetwork

# cidr_1 = IPNetwork('192.168.2.0/24')
# cidr_2 = IPNetwork('192.168.3.0/24')
# cidr_3 = IPNetwork('192.168.1.0/22')
#
# cidr = netaddr.cidr_merge([cidr_1, cidr_2, cidr_3])
#
# print(cidr)

raw = open('china-ip.txt').read().splitlines()
# print(len(raw))

ips = [IPNetwork(x) for x in raw]
print(len(ips))

ret = netaddr.cidr_merge(ips)
# print(ret)

print(len(ret))
