# -*- coding:utf-8 -*-
#!/usr/bin/python


#url管理器类
class UrlManager(object):
    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()

    def getNewUrls(self):
        return self.newUrls

    def getOldUrls(self):
        return self.oldUrls

    #添加新的url进urls
    def addNewUrl(self, url):
        if url is None:
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    #添加多条url进urls
    def addNewUrls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addNewUrl(url)

    #添加多条url进oldUrls
    def addOldUrls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.oldUrls.add(url)

    #检查是否还有新的url
    def hasNewUrl(self):
        if len(self.newUrls) == 0:
            return False
        return True

    #获取一条新的url
    def getNewUrl(self):
        url = self.newUrls.pop()
        self.oldUrls.add(url)
        return url
