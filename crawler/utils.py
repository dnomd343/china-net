#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import requests
from abc import ABC
from logger import logger
from requests import adapters
from abc import abstractmethod

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'


class Crawler(ABC):
    def __init__(self, name: str):
        self.__name = name
        logger.info(f'Create new crawler -> `{name}`')

    @abstractmethod
    def fetch(self) -> None:
        """ Fetch remote assets and dump as JSON format. """

    def _request(self, url: str) -> str:
        logger.debug(f'Crawler `{self.__name}` send http request -> `{url}`')
        try:
            session = requests.Session()
            adapter = adapters.HTTPAdapter(max_retries=3)
            [session.mount(f'{x}://', adapter) for x in {'http', 'https'}]
            request = session.get(url, timeout=20, headers={'User-Agent': UA})
            request.raise_for_status()
        except Exception as err:
            logger.error(f'Request `{url}` with error -> {err}')
            sys.exit(1)
        logger.info(f'Crawler `{self.__name}` request `{url}` -> {len(request.text)} bytes')
        return request.text

    def _dump(self, data: list[dict]) -> None:
        logger.info(f'Crawler `{self.__name}` fetch complete -> {len(data)} items')
        dump_file = os.path.join('release/raw/', f'{self.__name}.json')
        os.makedirs('release/raw/', exist_ok=True)

        lines = [f'  {json.dumps(x, ensure_ascii=False)}' for x in data]
        with open(dump_file, 'w') as fp:
            fp.write(f'[\n{',\n'.join(lines)}\n]\n')
        logger.info(f'Crawler `{self.__name}` dump file -> `{dump_file}`')
