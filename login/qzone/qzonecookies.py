import random
import time

import requests
from requests.cookies import RequestsCookieJar


class QZoneCookies(object):
    def __init__(self, username, password, browser):
        self.browser = browser
        self.username = username
        self.password = password

    def main(self):
        try:
            self.browser.get("https://qzone.qq.com/")
            self.browser.switch_to.frame('login_frame')  # 切换到登陆界面
            self.browser.find_element_by_id('switcher_plogin').click()  # 选择帐号密码登陆
            time.sleep(random.random() * 3)
            self.browser.find_element_by_name('u').clear()
            time.sleep(random.random() * 3)
            self.browser.find_element_by_name('u').send_keys(self.username)  # 此处输入你的QQ号
            time.sleep(random.random() * 3)
            self.browser.find_element_by_name('p').clear()
            time.sleep(random.random() * 3)
            self.browser.find_element_by_name('p').send_keys(self.password)  # 此处输入你的QQ密码
            time.sleep(random.random() * 3)
            self.browser.find_element_by_id('login_button').click()  # 点击登陆按键
            time.sleep(8)
            cookie_jar = RequestsCookieJar()
            for item in self.browser.get_cookies():
                key = item['name']
                cookie_jar.set(item['name'], item['value'], domain=item['domain'])
            self.browser.close()
            cookies = requests.utils.dict_from_cookiejar(cookie_jar)
            # cookies['qzone_cookie_jar'] = cookie_jar
            return {
                'status': 1,
                'content': cookies
            }
        except:
            return {
                'status': 3,
                'content': '登录失败'
            }
