# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import time
import pymysql
import re

def Insert(num, name, ac):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root",
                         "daliang", "test", use_unicode=True, charset="utf8")
    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    #sql语句 向表insert
    sql = "insert into cf456(no, name, ac) values ('%s', '%s', '%s')"\
          % (num, name, ac)
    try:
        cur.execute(sql)  # 执行sql语句
        db.commit()

    except Exception as e:
        raise e

    finally:
        db.close()  # 关闭连接

# url = 'http://codeforces.com/contest/912/standings/page/xx'

num = 0

for i in range(1, 23):
    html = urllib.request.urlopen('http://codeforces.com/contest/912/standings/page/%d' % i)
    soup = BeautifulSoup(html, 'lxml')
    print('------当前第%d页------' % i)

    table = soup.find_all('table', class_='standings')  # 通过此方法可以抓取标签
    table  = table[0]
    tr = table.find_all('tr')
    j = 0

    for i in tr:
        j += 1
        if j == 1 or j == 202: #去掉第一个和最后一个tr
            continue
        num += 1
        # print(num)

        a = i.find_all('a')
        a = a[0]
        name = a.get('title')
        # print(name)

        td = i.find_all('td') #算过题数
        # print(td)
        accept = 0
        for k in td:
            temp = str(k.get('title'))
            if re.match(r'^Passed', temp): #通过观察，通过的题目会有Passed System Test...，使用正则判一下
                accept += 1
        # print(accept)

        Insert(num, name, accept)

    time.sleep(0.5)