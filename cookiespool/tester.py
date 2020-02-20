# -*- coding: utf-8 -*-

import json

import requests
from requests.exceptions import ConnectionError

from .db import *


class ValidTester(object):
    def __init__(self, website='default'):
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)

    def test(self, username, cookies):
        raise NotImplementedError

    def run(self):
        cookies_groups = self.cookies_db.all()
        for username, cookies in cookies_groups.items():
            self.test(username, cookies)


class WeiboValidTester(ValidTester):
    def __init__(self, website='weibo'):
        ValidTester.__init__(self, website)

    def test(self, username, cookies):
        print('Testing Cookies', 'username', username)
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print('Cookies is invalid', username)
            self.cookies_db.delete(username)
            print('Deleted Cookies', username)
            return
        try:
            test_url = TEST_URL_MAP[self.website]
            response = requests.get(test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print('Cookies is valid', username)
            else:
                print(response.status_code, response.headers)
                print('Cookies is invalid', username)
                self.cookies_db.delete(username)
                print('Deleted Cookies', username)
        except ConnectionError as e:
            print('Exception', e.args)


class QZoneValidTester(ValidTester):
    def __init__(self, website='qzone'):
        ValidTester.__init__(self, website)

    def test(self, username, cookies):
        print('Testing Cookies', 'username', username)
        try:
            cookies = json.loads(cookies)
            # cookies.pop('qzone_cookie_jar')
        except TypeError:
            print('Cookies is invalid', username)
            self.cookies_db.delete(username)
            print('Deleted Cookies', username)
            return
        try:
            test_url = TEST_URL_MAP[self.website]
            response = requests.get(test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print('Cookies is valid', username)
            else:
                print(response.status_code, response.headers)
                print('Cookies is invalid', username)
                self.cookies_db.delete(username)
                print('Deleted Cookies', username)
        except ConnectionError as e:
            print('Exception ', e.args)


if __name__ == '__main__':
    WeiboValidTester().run()
