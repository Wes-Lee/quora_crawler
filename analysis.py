# -*- coding:utf-8 -*-
#!/usr/bin/python
"""
分析数据程序
"""

from pylab import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas.io.sql as sql
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
con = MySQLdb.connect(user='root', passwd='559559', db='db_quora_crawler', use_unicode=True, charset='utf8')
frame = sql.read_sql('select * from t_user', con)
con.close()

frame = frame.drop('id',axis=1)
frame = frame.set_index('name_id')
frame = frame.drop_duplicates()

#获得数据的平均数，中位数和标准差
def user_describe():
    print frame.describe()

#统计数据居住地国家人数
def user_live():
    #统计国家的主要城市的关键字
    America_name = ['Alabama', 'AL', 'Alaska', 'AK', 'Arizona', 'AZ', 'Arkansas', 'AR', 'California', 'CA', 'Colorado',
                    'CO', 'Connecticut', 'CT',
                    'Delaware', 'DE', 'District of columbia', 'DC', 'Florida', 'FL', 'Georgia', 'GA', 'Hawaii', 'HI',
                    'Idaho', 'ID', 'Illinois', 'IL',
                    'Indiana', 'IN', 'Iowa', 'IA', 'Kansas', 'KS', 'Kentucky', 'KY', 'Louisiana', 'LA', 'Maine', 'ME',
                    'Massachusetts', 'MA', 'Michigan',
                    'MI', 'Minnesota', 'MN', 'St.Paul', 'Mississippi', 'MS', 'Missouri', 'MO', 'Montana', 'MT',
                    'Nebraska', 'NE', 'Nevada', 'NV', 'Ohio',
                    'OH', 'New Hampshire', 'NH', 'New Jeresy', 'NJ', 'New Mexico', 'NM', 'New York', 'NY',
                    'NorthCarolina', 'NC', 'North Dakota', 'ND',
                    'Oklahoma', 'OK', 'Oregon', 'OR', 'Pennsylvania', 'PA', 'Rhode Island', 'RI', 'SouthCarolina', 'SC',
                    'South Dakota', 'SD', 'Tennessee',
                    'TN', 'Texas', 'TX', 'Utah', 'UT', 'Vermont', 'VT', 'Virginia', 'VA', 'Washington', 'WA',
                    'West Virginia', 'WV', 'Wisconsin', 'WI',
                    'Wyoming', 'WY', 'America', 'US', 'USA', 'U.S.A', 'U.S']

    China_name = ['China', 'CHN', 'HongKong', 'Macau', 'Taipei', 'Taiwan', 'Shanghai', 'Beijing', 'Shenzhen',
                  'Guangzhou', 'Tianjin', 'Naijing', 'Wuhan',
                  'Hangzhou', 'Chongqing', 'Suzhou', 'Dalian', 'Dongguan', 'Shenyang', 'Chengdu', 'Qingdao', 'Xiamen',
                  'Foshan', 'Jinan', 'Harbin', "xi'an",
                  'Kunming', 'Wuxi', 'Fuzhou', 'Ningbo', 'Zhuhai', 'Zhongshan', 'Changsha', 'Changchun', 'Wenzhou',
                  'Hefei', 'Zhengzhou', 'Shijiazhuang'
                                        'Haikou', 'Huizhou', 'Changzhou', 'Daqing', 'Nanchang', 'Shaoxing', 'Nantong',
                  'Yantai', 'Guiyang', 'Lanzhou', 'Nanning', 'Jiaxing',
                  'Weihai', 'Quanzhou']

    India_name = ['India', 'IND', 'Mumbai', 'Delhi', 'Kolkata', 'Bangalore', 'Chennai', 'Ahmadabad', 'Hyderabad',
                  'Pune', 'Kanpur', 'Surat', 'Jaipur',
                  'Lucknow', 'Nagpur', 'Indore', 'Bhopur', 'Ludhiana', 'Patna', 'Vadodara', 'Thana', 'Agra', 'Kalyan',
                  'Varanasi', 'Nashik', 'Meerut',
                  'Faridabad', 'Howrah', 'Pimpri-Chinchwad', 'Allahabad', 'Amritsar', 'Visakhapatnam', 'Ghaziabad',
                  'Rajkot', 'Jabalpur', 'Coimbatore',
                  'Madurai', 'Srinagar', 'Vijayawada']

    English_name = ['UK', 'U.K', 'British', 'Bath', 'Birmingham', 'Bradford', 'Brighton & Hove', 'Bristol', 'Cambridge',
                    'Canterbury', 'Carlisle',
                    'Chester', 'Chichester', 'Coventry', 'Derby', 'Durham', 'Ely', 'Exeter', 'Gloucester', 'Hereford',
                    'Kingston-upon-Hull', 'Leeds',
                    'Lancaster', 'Leicester', 'Lichfield', 'Lincoln', 'Liverpool', 'London', 'Manchester',
                    'Newcastle upon Tyne', 'Norwich', 'Oxford',
                    'Nottingham', 'Peterborough', 'Plymouth', 'Portsmouth', 'Preston', 'Ripon', 'Salford', 'Salisbury',
                    'Sheffield', 'Southampton',
                    'St Albans', 'Stoke-on-Trent', 'Sunderland', 'Truro', 'Wakefield', 'Wells', 'City of Westminster',
                    'Winchester', 'Wolverhampton',
                    'Worcester', 'York']

    Australia_name = ['Australia', 'Canberra', 'Melbourne', 'Sydney', 'Geelong', 'Adelaide', 'Brisbane', 'Townsville',
                      'Darwin', 'Perth', 'Newcastle']

    live = frame['live']

    live_list = live.values
    America = 0
    China = 0
    India = 0
    UK = 0
    Australia = 0
    live_other = 0
    live_unknow = 0

    for temp in live_list:
        flag = 0
        for name in America_name:
            if flag == 1:
                break
            if name in temp:
                America += 1
                flag = 1
                break
        for name in India_name:
            if flag == 1:
                break
            if name in temp:
                India += 1
                flag = 1
                break
        for name in English_name:
            if flag == 1:
                break
            if name in temp:
                UK += 1
                flag = 1
                break
        for name in China_name:
            if flag == 1:
                break
            if name in temp:
                China += 1
                flag = 1
                break
        for name in Australia_name:
            if flag == 1:
                break
            if name in temp:
                Australia += 1
                flag = 1
                break
        if flag == 1:
            continue
        if 'unknow' in temp:
            live_unknow += 1
        else:
            live_other += 1

    live_dict1 = {'中国': China, '澳大利亚': Australia, '英国': UK, '美国': America, '印度': India, '其他': live_other,
                      '未知': live_unknow}
    live_dict2 = {'中国': China, '澳大利亚': Australia, '英国': UK, '美国': America, '印度': India, '其他': live_other}
    live_series1 = Series(live_dict1, index=['中国', '澳大利亚', '英国', '美国', '印度', '其他', '未知'])
    live_series2 = Series(live_dict2, index=['中国', '澳大利亚', '英国', '美国', '印度', '其他'])

    live_x1 = range(len(live_dict1))
    live_y1 = live_series1.values
    live_x2 = range(len(live_dict2))
    live_y2 = live_series2.values

    live_fig, live_ax = plt.subplots(1, 2)
    live_series1.plot(kind='bar', ax=live_ax[0], rot=0, color='b', alpha=0.3)
    live_ax[0].set_title('国家人数统计(含未知)')
    live_series2.plot(kind='bar', ax=live_ax[1], rot=0, color='b', alpha=0.3)
    live_ax[1].set_title('国家人数统计(不含未知)')

    for a, b in zip(live_x1, live_y1):
        live_ax[0].text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom')
    for a, b in zip(live_x2, live_y2):
        live_ax[1].text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom')

#统计数据学历人数
def user_school():
    PhD_name = ['P.h.D', 'Ph.D', 'PhD', 'MD', 'M.D', 'Doctor of']

    MS_name = ['M.S', 'MS', 'MBA', 'M.B.A', 'Master of']

    university_name = ['University', 'College']

    school = frame['school']
    school_list = school.values
    PhD = 0
    MS = 0
    university = 0
    school_unknow = 0
    school_other = 0

    for temp in school_list:
        flag = 0
        for name in PhD_name:
            if flag == 1:
                break
            if name in temp:
                flag = 1
                PhD += 1
                break
        for name in MS_name:
            if flag == 1:
                break
            if name in temp:
                flag = 1
                MS += 1
                break
        for name in university_name:
            if flag == 1:
                break
            if name in temp:
                flag = 1
                university += 1
                break
        if flag == 1:
            continue
        if 'unknow' in temp:
            school_unknow += 1
        else:
            school_other += 1

    school_dict1 = {'博士': PhD, '硕士': MS, '大学': university, '其他': school_other, '未知': school_unknow}
    {'博士': PhD, '硕士': MS, '大学': university, '其他': school_other}
    school_dict2 = {'博士': PhD, '硕士': MS, '大学': university, '其他': school_other, '未知': school_unknow}
    {'博士': PhD, '硕士': MS, '大学': university}
    school_series1 = Series(school_dict1, index=['博士', '硕士', '大学', '其他', '未知'])
    school_series2 = Series(school_dict2, index=['博士', '硕士', '大学', '其他'])

    school_x1 = range(len(school_dict1))
    school_y1 = school_series1.values
    school_x2 = range(len(school_dict2))
    school_y2 = school_series2.values

    school_fig, school_ax = plt.subplots(1, 2)
    school_series1.plot(kind='bar', ax=school_ax[0], rot=0, color='g', alpha=0.3)
    school_ax[0].set_title('学历统计(含未知)')
    school_series2.plot(kind='bar', ax=school_ax[1], rot=0, color='g', alpha=0.3)
    school_ax[1].set_title('学历统计(不含未知)')

    for a, b in zip(school_x1, school_y1):
        school_ax[0].text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom')
    for a, b in zip(school_x2, school_y2):
        school_ax[1].text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom')

#统计用户回答数
def user_answer_number():
    answer_number_series = frame['answer_number']
    print answer_number_series.describe()
    answer_zero_number = len(frame.ix[frame.answer_number == 0])
    answer_zero_more_number = len(frame.ix[(frame.answer_number < 10) & (frame.answer_number != 0)])
    answer_ten_more_number = len(frame.ix[(frame.answer_number >= 10) & (frame.answer_number < 100)])
    answer_hundred_more_number = len(frame.ix[(frame.answer_number >= 100) & (frame.answer_number < 1000)])
    answer_thousand_more_number = len(frame.ix[(frame.answer_number >= 1000)])

    answer_list = [answer_zero_number, answer_zero_more_number, answer_ten_more_number, answer_hundred_more_number,
                   answer_thousand_more_number]
    answer_labels = ['0回答数', '0~10回答数', '10~100回答数', '100~1000回答数', '1000以上']
    expl = [0, 0.2, 0.2, 0.2, 0.2]
    plt.pie(answer_list, labels=answer_labels, autopct='%1.1f%%', explode=expl, pctdistance=0.8, shadow=True)
    plt.title('回答数统计', bbox={'facecolor': '0.8', 'pad': 5})

#统计用户关注话题数
def user_topics_number():
    topics_number_series = frame['topics_number']
    print topics_number_series.describe()
    topics_zero_number = len(frame.ix[(frame.topics_number == 0)])
    topics_zero_more_number = len(frame.ix[(frame.topics_number > 0) & (frame.topics_number < 10)])
    topics_ten_more_number = len(frame.ix[(frame.topics_number >= 10) & (frame.topics_number < 100)])
    topics_hundred_more_number = len(frame.ix[(frame.topics_number >= 100) & (frame.topics_number < 1000)])
    topics_thousand_more_number = len(frame.ix[(frame.topics_number >= 1000)])

    topics_list = [topics_zero_number, topics_zero_more_number, topics_ten_more_number, topics_hundred_more_number,
                   topics_thousand_more_number]
    topics_labels = ['等于0', '0~10', '10~100', '100~1000', '大于1000']
    expl = [0, 0.2, 0.2, 0.2, 0.2]
    plt.pie(topics_list, labels=topics_labels, autopct='%1.1f%%', explode=expl, pctdistance=0.8, shadow=True)
    plt.title('关注话题数数统计', bbox={'facecolor': '0.8', 'pad': 5})

#用户索引与粉丝数
def user_follower_number():
    follower_number = frame.follower_number
    follower_number = follower_number.sort_values(ascending=False)
    follower_number = follower_number.reset_index(range(119768)).drop('name_id', axis=1)

    plt.xlabel('用户索引')
    plt.ylabel('用户粉丝数')
    plt.scatter(follower_number.index, follower_number.values)

#用户索引与回答阅览数
def user_answer_view():
    answer_view = frame.answer_view
    answer_view = answer_view.sort_values(ascending=False)
    answer_view = answer_view.reset_index(range(119768)).drop('name_id', axis=1)

    plt.xlabel('用户索引')
    plt.ylabel('回答阅览数')
    plt.scatter(answer_view.index, answer_view.values)

#用户粉丝数与回答数
def answer_number_follower():
    answer_number = np.log10(frame.answer_number)
    follower_number = np.log10(frame.follower_number)

    follower_number_and_answer_number = frame.follower_number.corr(frame.answer_number[answer_number > 0])
    plt.xlabel('用户回答数')
    plt.ylabel('用户粉丝数')
    plt.scatter(follower_number, answer_number)
    print follower_number_and_answer_number

#用户粉丝数与回答浏览数
def follower_answer_view():
    follower_number = np.log10(frame.follower_number)
    answer_view = np.log10(frame.answer_view)

    answer_view_and_follower_number = frame.follower_number.corr(frame.answer_view[answer_view > 0])
    plt.xlabel('用户粉丝数')
    plt.ylabel('回答阅览量')
    plt.scatter(follower_number, answer_view)
    print answer_view_and_follower_number

#用户回答数与回答阅览数
def answer_number_answer_view():
    answer_number = np.log10(frame.answer_number)
    answer_view = np.log10(frame.answer_view)

    answer_view_and_answer_number = frame.answer_view[answer_view > 0].corr(frame.answer_number[answer_number > 0])
    plt.xlabel('用户回答数')
    plt.ylabel('回答阅览量')
    plt.scatter(answer_number, answer_view)

    print answer_view_and_answer_number