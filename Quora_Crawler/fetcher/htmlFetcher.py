# -*- coding:utf-8 -*-
#!/usr/bin/python
import requests

class HtmlFetcher(object):
    #通过浏览器获取网页html源码
    # def getHtmlByDriver(self, driver, url):
    #     driver.get(url)
    #     driver.scrollDown()
    #     return driver.page_source

    #通过Requests获取网页html源码
    def getHtmlByRequests(self, cookies, url):
        requests.adapters.DEFAULT_RETRIES = 5
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        cookieDict = {}
        for cookie in cookies:
            name = cookie['name']
            value = cookie['value']
            cookieDict[name] = value
        request = requests.get(url, cookies=cookieDict, headers=headers, timeout=5)
        if request.status_code != 200:
            raise Exception('获取网页失败')
        source = request.text
        request.close()
        return source

