#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from asn.union import AsnUnion


if __name__ == '__main__':
    kk = AsnUnion()
    for x in kk.export():
        # print(x.desc)
        print(x.asn, '->', x.v4_active, ' | ', x.v6_active, ' | ', x.rank)
