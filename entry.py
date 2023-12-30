#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logger import logger

from crawler.fries import Fries

if __name__ == '__main__':
    Fries().fetch()

    # logger.debug('DEBUG')
    # logger.info('INFO')
    # logger.warning('WARN')
    # logger.error('ERROR')
    # logger.critical('CRITICAL')
