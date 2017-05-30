# -*- coding:utf-8 -*-
#!/usr/bin/python

import urllib2
import time
from Quora_Crawler.manager.urlManager import UrlManager
from Quora_Crawler.fetcher.driver import Driver
from Quora_Crawler.fetcher.htmlFetcher import HtmlFetcher
from Quora_Crawler.parser.htmlParser import HtmlParser
from Quora_Crawler.database.mysql import Saver

#调度主程序类
class CrawlerMain(object):
    def __init__(self):
        self.urlMananger = UrlManager()
        self.driver = Driver()
        self.fetcher = HtmlFetcher()
        self.parser = HtmlParser()
        self.saver = Saver()

    def craw(self, userName, password):
        cookies = self.driver.logIn(userName, password)
        self.driver.quit()
        newUrls = self.saver.getNewUrls()
        count, oldUrls = self.saver.getOldUrls()
        self.urlMananger.addOldUrls(oldUrls)
        count += 1
        self.urlMananger.addNewUrls(newUrls)
        while self.urlMananger.hasNewUrl():
            try:
                if count > 120000:
                    break
                homeUrl = self.urlMananger.getNewUrl()
                Url = homeUrl + '/following'
                print '正在爬取第%d条 url:%s' % (count, homeUrl.encode('utf-8'))
                source = self.fetcher.getHtmlByRequests(cookies, Url)
                urls, user = self.parser.parse(homeUrl, source)
                self.saver.saveNewUrl(urls)
                self.urlMananger.addNewUrls(urls)
                self.saver.saveUser(user)
                self.saver.useUrl(homeUrl)
                count += 1

            except Exception, e:
                time.sleep(1)
                try:
                    urllib2.urlopen('https://www.baidu.com')
                except Exception:
                    print '网络连接失败'
                    break
                print e.message

#爬虫启动主程序
if __name__ == '__main__':
    rootUrl = 'https://www.quora.com/profile/Oliver-Emberton'
    userName = '15914165757@163.com'
    password = '559-ljw'
    crawler = CrawlerMain()
    crawler.craw(userName, password)
    print '爬取结束'
