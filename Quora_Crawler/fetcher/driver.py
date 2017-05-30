# -*- coding:utf-8 -*-
#!/usr/bin/python

import time
from bs4 import BeautifulSoup
from selenium import webdriver

"""模拟浏览器登陆以及下拉页面"""

class Driver(webdriver.PhantomJS):
    def __init__(self):
        super(Driver, self).__init__(service_args=['--load-images=false'])

    #浏览器模拟登陆方法
    def logIn(self, email, password):
        self.get('https://www.quora.com/')
        source = self.page_source
        #寻找用户名框，密码框和登陆键的id
        soup = BeautifulSoup(source, 'lxml')
        for temp in soup.find_all('input', class_='text header_login_text_box ignore_interaction'):
            w2cid = temp.get('w2cid')
        #定位用户名框，密码框和登陆键后登陆
        userName = self.find_element_by_id('__w2_'+w2cid+'_email')
        passWord = self.find_element_by_id('__w2_'+w2cid+'_password')
        userName.send_keys(email)
        passWord.send_keys(password)
        time.sleep(6)
        self.find_element_by_id('__w2_'+w2cid+'_submit_button').click()
        time.sleep(6)
        if 'Home - Quora' not in self.page_source:
            self.quit()
            raise Exception('登陆失败')
        print '登陆成功'
        return self.get_cookies()

    #模拟浏览器滚动条下拉
    # def scrollDown(self):
    #     src_updated = self.page_source
    #     src = ""
    #     while src != src_updated:
    #         src = src_updated
    #         self.execute_script("var q=document.body.scrollTop+=10000")
    #         time.sleep(.5)
    #         if src_updated == self.page_source:
    #             time.sleep(1)
    #             self.execute_script("var q=document.body.scrollTop+=10000")
    #         src_updated = self.page_source
