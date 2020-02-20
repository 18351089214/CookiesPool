# -*- coding: utf-8 -*-

from .db import RedisClient

conn = RedisClient('accounts', 'weibo')


def set(account, sep='----'):
    username, password = account.split(sep)
    result = conn.set(username, password)
    print('Account', username, 'Password', password)
    print('Succeeded to input' if result else 'Failed to input')


def scan():
    print('Please input account&password, input exit to terminate')
    while True:
        account = input()
        if account == 'exit':
            break
        set(account)


if __name__ == '__main__':
    scan()
