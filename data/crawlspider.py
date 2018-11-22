import requests
from lxml import etree
from pyquery import PyQuery as pq
import pymysql
import time
import json


dock = set()


def get_data():
    base_url = 'https://www.jin10.com'

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "ZH-cn,zh;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "if-none-match": 'W/"06C4F4ABF8FAF6805F8E20609189B101-1"',
        "referer": "https://www.jin10.com/baojia.php?jsonpcallbacK=jquery11110685496690622664_1542676119249&type=xagusd&_=1542676119254",
        "upgrade-insecure-requests": "1",
        "user-agent": "mozilla/5.0 (windoWS NT 10.0; Win64; x64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/70.0.3538.102 safari/537.36",
    }

    html = requests.get(base_url, headers=headers)
    # html.encoding('utf-8')
    html.encoding = html.apparent_encoding  # 转码
    if html.status_code == 200:
        # print(html.headers)
        # print(html.text)
        html = html.text
        # html = etree.HTML(html)
        html = pq(html)
        # info_time = html.xpath('//div[@class="jin-flash_list"]//div[@class="jin-flash_time"]/text()')
        # info_text = html.xpath('//div[@class="jin-flash_list"]//div[@class="jin-flash_wrap J_flash_wrap"]//p[@class="J_flash_text"]/text()')

        infos = html('.jin-flash_list').items()
        for info in infos:
            # print(info)
            info_li = info('.jin-flash_item').items()

            for info_de in info_li:
                info_time = info_de('.jin-flash_h')
                info_text = info_de('.jin-flash_b')
                info_url = info_de('.jin-flash_icon a')
                info_url = info_url.attr('href')

                info_time = info_time.text()
                info_text = info_text.text()
                # print(info_id)
                # print(info_time)
                # print(info_text)
                # print(info_url)
                front_num = len(dock)
                # print(front_num)
                dock.add(info_url)
                behind_num = len(dock)
                # print(behind_num)
                if front_num + 1 == behind_num:
                    item = {'info_url': info_url,
                            'info_time': info_time,
                            'info_text': info_text,
                            'get_time': time.strftime("%Y-%m-%d %H:%M:%S"),
                            'data_source': u'金十数据',
                            }
                    print(item)
                    # saveurl(info_url)
                    savemysql(item)
                else:
                    # print('重复数据')
                    pass

    else:
        print(html.status_code)


def saveurl(parm):
    with open(r'D:\Users\Dong\Desktop\mysite\data\sign.txt', 'r') as f:
        f.write(parm+"\n")


def savemysql(item):
    conn = pymysql.connect(host='127.0.0.1', db='py08', user='root', password='123456', charset='utf8')
    cur = conn.cursor()

    sql = 'insert into news_news(info_url,info_time,info_text,get_time,data_source) VALUES(%s,%s,%s,%s,%s)'
    data = (item['info_url'], item['info_time'], item['info_text'], item['get_time'], item['data_source'])
    try:
        cur.execute(sql, data)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print('error:', e)

    cur.close()
    conn.close()


if __name__ == "__main__":
    # with open(r'D:\Users\Dong\Desktop\mysite\data\sign.txt', 'r') as f:
    #     f.read()
    while True:
        get_data()
        time.sleep(60)
