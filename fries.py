#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
from typing import Generator

url = 'https://github.com/VirgilClyne/GetSomeFries/raw/main/ruleset/ASN.China.list'

# data = requests.get(url)
#
# print(data.text)
#

content = open('ASN.China.list').read()

def parse(raw: str) -> Generator[tuple[bool, int, str], None, None]:
    for line in raw.splitlines():
        if line.startswith('IP-ASN'):
            if match := re.match(r'^IP-ASN, *(\d+) *//(.+)$', line):
                yield True, int(match[1]), match[2].strip()
        elif line.startswith('# IP-ASN'):
            if match := re.match(r'^# *IP-ASN, *(\d+) *//(.+)$', line):
                yield False, int(match[1]), match[2].strip()


ret = parse(content)

for kk in [x for x in ret]:
    print(kk)
