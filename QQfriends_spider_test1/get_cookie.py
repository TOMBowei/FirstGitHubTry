from selenium import webdriver
from time import sleep
import json
import re
import urllib
import requests

driver = webdriver.Chrome()
driver.get('https://user.qzone.qq.com/596746772/myhome/friends')

#切换到登录的框架
driver.switch_to.frame('login_frame')
#找到账号密码登陆的地方
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('596746772')
driver.find_element_by_id('p').send_keys('Boweiwu0318')
driver.find_element_by_id('login_button').click()
#保存本地的cookie
sleep(10)
cookies = driver.get_cookies()
# print(cookies)
cookie_dic = {}
for cookie in cookies:
    if 'name' in cookie and 'value' in cookie:
        cookie_dic[cookie['name']] = cookie['value']
    with open('cookie_dict.txt', 'w') as f:
        json.dump(cookie_dic, f)
        # print(cookie_dic)

