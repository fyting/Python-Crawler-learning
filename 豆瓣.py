# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import time
import pymysql

def Insert(num, href, name, intro):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root",
                         "daliang", "test", use_unicode=True, charset="utf8")
    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    #sql语句 向表insert
    sql = "insert into book(no, href, name, content) values ('%s', '%s', '%s', '%s')"\
          % (num, href, name, intro)
    try:
        cur.execute(sql)  # 执行sql语句
        db.commit()

    except Exception as e:
        raise e

    finally:
        db.close()  # 关闭连接

num = 0
start_time = time.time()

url = 'https://read.douban.com/columns/category/all?sort=hot&start='

for i in range(0,5000,10):
    #urllib.request库用来向该网服务器发送请求，请求打开该网址链接
    html = urllib.request.urlopen('https://read.douban.com/columns/category/all?sort=hot&start=%d' % i)
    #BeautifulSoup库解析获得的网页，第二个参数一定记住要写上‘lxml’，记住就行
    soup = BeautifulSoup(html,'lxml')

    print('==============' + '第%d页' % (i / 10 + 1) + '==============')

    # h4_node_list = soup.find_all('h4')
    # for i in h4_node_list:
    #
    #     num = num + 1
    #     href_ = i.find_all('a')
    #     href_ = href_[0]
    #     href = href_.get('href')
    #     print(href)
    #     str = i.string
    #     print('第%d本书' % num, '<<' + str + '>>')
    #
    # time.sleep(1)

    info = soup.find_all('div', class_='info') #通过此方法可以抓取到div标签
    for i in info:
        num += 1

        h4 = i.find_all('h4')
        h4 = h4[0]
        hreftemp = h4.find_all('a')
        hreftemp = hreftemp[0]
        href = hreftemp.get('href')
        name = '<<' + h4.string + '>>'
        # print(href, name)

        intro = i.find_all('div', class_='intro')
        intro = intro[0]
        intro = intro.get_text()
        # print(intro)

        Insert(num, href, name, intro)

    time.sleep(0.5)

end_time = time.time()
duration_time = end_time - start_time
print('运行时间共：%.2f' % duration_time + '秒')
print('共抓到%d本书名' % num)