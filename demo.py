#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from asn.union import AsnUnion


if __name__ == '__main__':
    kk = AsnUnion()
    for x in kk.export():
        # x.desc
        # x.is_active
        x.rank
