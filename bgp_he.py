#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

url = 'https://bgp.he.net/country/CN'

ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

content = open('CN.html').read()


def parse(raw: str):
    body = BeautifulSoup(raw, 'lxml')
    table = body.find('table', id='asns').find('tbody')
    for row in table.find_all('tr'):
        info = [x.text for x in row.find_all('td')]
        asn = int(info[0].removeprefix('AS'))
        nums = [int(x.replace(',', '')) for x in info[2:6]]
        yield asn, info[1].strip(), *nums


kk = parse(content)

for line in kk:
    print(line)

# print(len([x for x in kk]))
