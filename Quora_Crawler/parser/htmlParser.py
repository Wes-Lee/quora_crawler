# -*- coding:utf-8 -*-
#!/usr/bin/python

import re
from bs4 import BeautifulSoup
from Quora_Crawler.po.user import User

#html解析器类
class HtmlParser(object):

    #从主页解析信息
    def parse(self, homeUrl, Source):
        soup = BeautifulSoup(Source, 'lxml')
        #解析取得nameId
        nameId = homeUrl.replace('https://www.quora.com/profile/', '')
        #解析取得name
        nameNode = soup.find_all('span', class_='user')[2]
        name = nameNode.get_text()
        #解析取得学校
        schoolNode = soup.select('div[class="layout_3col_right"] div[class="CredentialListItem AboutListItem SchoolCredentialListItem"] '
                                 'span[class="UserCredential IdentityCredential"]')
        school = 'unknow'
        if len(schoolNode) != 0:
            school = schoolNode[0].get_text()
        #解析取得居住地
        liveNode = soup.select('div[class="layout_3col_right"] div[class="CredentialListItem LocationCredentialListItem AboutListItem"] '
                                 'span[class="UserCredential IdentityCredential"]')
        live = 'unknow'
        if len(liveNode) != 0:
            live = liveNode[0].get_text()
        #解析取得回答数
        answerNumNode = soup.select('li[class="EditableListItem NavListItem NavItem AnswersNavItem not_removable"] '
                                     'span[class="list_count"]')
        answerNum = int(answerNumNode[0].get_text().replace(',', ''))
        #解析取得发起问题数
        questionNumNode = soup.select('li[class="EditableListItem QuestionsNavItem NavItem NavListItem not_removable"] '
                                      'span[class="list_count"]')
        questionNum = int(questionNumNode[0].get_text().replace(',', ''))
        #解析取得关注的人数
        followingNumNode = soup.select('li[class="FollowingNavItem NavListItem NavItem EditableListItem not_removable"] '
                                       'span[class="list_count"]')
        followingNum = int(followingNumNode[0].get_text().replace(',', ''))
        #解析取得粉丝数
        followerNumNode = soup.select('li[class="EditableListItem NavListItem FollowersNavItem NavItem not_removable"] '
                                       'span[class="list_count"]')
        followerNum = int(followerNumNode[0].get_text().replace(',', ''))
        #解析取得关注话题数
        topicsNumNode = soup.select('li[class="EditableListItem TopicsNavItem NavItem NavListItem not_removable"] '
                                       'span[class="list_count"]')
        topicsNum = int(topicsNumNode[0].get_text().replace(',', ''))
        #解析取得回答浏览总数
        answerViewNode = soup.select('div[class="AboutListItem AnswerViewsAboutListItem"] '
                                     'span[class="main_text"]')
        answerViewNum = 0
        if len(answerViewNode) != 0:
            answerView = (answerViewNode[0].get_text().split())[0]
            if re.match(r'.*k$', answerView):
                num = float(answerView.replace('k', ''))
                num *= 1000
            elif re.match(r'.*m$', answerView):
                num = float(answerView.replace('m', ''))
                num *= 1000000
            answerViewNum = int(num)

        user = User(nameId, name, school, live, followingNum, followerNum, questionNum, answerNum, topicsNum, answerViewNum, homeUrl)
        name_node = soup.find_all('a', class_ ='user', href=re.compile(r'/profile/.*'))
        urls = []
        for node in name_node:
            url = 'https://www.quora.com' + node['href']
            urls.append(url)
        return urls, user
