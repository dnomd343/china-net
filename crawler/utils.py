#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
from abc import ABC
from abc import abstractmethod

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'


class Crawler(ABC):
    def __init__(self, name: str):
        self.__name = name

    @abstractmethod
    def fetch(self) -> None:
        """ Fetch remote assets and dump as JSON format. """

    def _request(self, url: str) -> str:
        req = requests.get(url, headers={'User-Agent': UA})
        print(self.__name, len(req.text))
        return req.text

    def _dump(self, data: list) -> None:
        with open(f'{self.__name}.json', 'w') as fp:
            fp.write(json.dumps(data, indent=2, ensure_ascii=False))
            fp.write('\n')
