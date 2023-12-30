#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

url = 'https://whois.ipip.net/iso/CN'


def parse(raw: str):
    table = BeautifulSoup(content, 'lxml').find('table')
    table.find('thead').clear()
    for row in table.find_all('tr'):
        info = [x.text for x in row.find_all('td')]
        asn = int(info[0].removeprefix('AS'))
        to_int = lambda x: int(x.replace(',', ''))
        yield asn, info[1].strip(), to_int(info[2]), to_int(info[3])


content = open('IPIP-CN.html').read()

kk = parse(content)

for line in kk:
    print(line)
