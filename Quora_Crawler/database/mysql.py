# -*- coding:utf-8 -*-
#!/usr/bin/python

import MySQLdb

#mysql储存类
class Saver(object):
    def saveUser(self, user):
        con = MySQLdb.connect(user='root', passwd='559559', db='db_quora_crawler', use_unicode=True, charset='utf8')
        cur = con.cursor()
        cur.execute('INSERT INTO t_user VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' , user.getList())
        con.commit()
        cur.close()
        con.close()

    def saveNewUrl(self, urls):
        con = MySQLdb.connect(user='root', passwd='559559', db='db_quora_crawler', use_unicode=True, charset='utf8')
        cur = con.cursor()
        for url in urls:
            cur.execute('INSERT INTO t_new_urls VALUES (NULL, %s)', [url])
        con.commit()
        cur.close()
        con.close()

    def useUrl(self, url):
        con = MySQLdb.connect(user='root', passwd='559559', db='db_quora_crawler', use_unicode=True, charset='utf8')
        cur = con.cursor()
        cur.execute('INSERT INTO t_old_urls VALUES (NULL, %s)', [url])
        con.commit()
        cur.close()
        con.close()

    def getNewUrls(self):
        con = MySQLdb.connect(user='root', passwd='559559', db='db_quora_crawler', use_unicode=True, charset='utf8')
        cur = con.cursor()
        cur.execute('SELECT new_url FROM t_new_urls')
        urls = []
        for temp in cur.fetchall():
            urls.append(temp[0])
        cur.close()
        con.close()
        return urls

    def getOldUrls(self):
        con = MySQLdb.connect(user='root', passwd='559559', db='db_quora_crawler', use_unicode=True, charset='utf8')
        cur = con.cursor()
        cur.execute('SELECT old_url FROM t_old_urls')
        urls = []
        for temp in cur.fetchall():
            urls.append(temp[0])
        cur.execute('SELECT MAX(id) FROM t_old_urls')
        count = cur.fetchall()[0][0]
        cur.close()
        con.close()
        return count, urls

