# -*- coding:utf-8 -*-
#!/usr/bin/python

#用户类
class User(object):
    def __init__(self, nameId, name, school, live, followingNum, followerNum, questionNum, answerNum, topicsNum, answerView, url):
        self.__nameId = nameId
        self.__name = name
        self.__school = school
        self.__live = live
        self.__followingNumber = followingNum
        self.__followerNumber = followerNum
        self.__questionNumber = questionNum
        self.__answerNumber = answerNum
        self.__topicsNumber = topicsNum
        self.__answerView = answerView
        self.__url = url

    def getList(self):
        userList = []
        userList.append(self.__nameId.encode('utf-8'))
        userList.append(self.__name.encode('utf-8'))
        userList.append(self.__school.encode('utf-8'))
        userList.append(self.__live.encode('utf-8'))
        userList.append(self.__followingNumber)
        userList.append(self.__followerNumber)
        userList.append(self.__questionNumber)
        userList.append(self.__answerNumber)
        userList.append(self.__topicsNumber)
        userList.append(self.__answerView)
        userList.append(self.__url.encode('utf-8'))
        return userList

    def getNameId(self):
        return self.__nameId

    def getName(self):
        return self.__name

    def getFollowingNum(self):
        return self.__followingNumber

    def getFollowerNum(self):
        return self.__followerNumber

    def getQuestionNum(self):
        return self.__questionNumber

    def getAnswerNum(self):
        return self.__answerNumber

    def getTopicsNumber(self):
        return self.__topicsNumber

    def getAnswerView(self):
        return self.__answerView

    def getUrl(self):
        return self.__url