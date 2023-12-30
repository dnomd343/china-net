#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
import colorlog


def build_handle() -> logging.Handler:
    handle = colorlog.StreamHandler()
    handle.setFormatter(colorlog.ColoredFormatter(
        '%(light_black)s%(asctime)s.%(msecs)03d%(log_color)s '
        '[%(levelname)s] %(message)s (%(module)s.%(funcName)s:%(lineno)d)',
        datefmt='%Y-%m-%d %H:%M:%S',
        stream=sys.stderr
    ))
    handle.setLevel(logging.DEBUG)
    return handle


logger = logging.getLogger()
logger.addHandler(build_handle())
logger.setLevel(logging.DEBUG)
