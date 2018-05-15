#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import time

__author__ = "wwcom123"

url_path = [
    "video/001.html",
    "video/002.html",
    "video/003.html",
    "video/004.html",
    "video/005.html",
    "video/006.html",
    "audio/001.html",
    "audio/002.html",
    "book/001.html",
    "book/002.html",
    "book/003.html"
]

ip_slices = [28,32,133,10,47,178,188,68,79,232,158,168,192,98,72,55]

search_engine = [
    "http://www.baidu.com/s?wd={query}",
    "http://www.sougou.com/web?query={query}",
    "http://cn.bing.com/search?q={query}",
    "http://search.yahoo.com/search?p={query}"
]

search_keyword = [
    "小猪佩奇",
    "汪汪队立大功",
    "海底小纵队",
    "萌鸡小队",
    "爱探险的朵拉"
]

http_status = ["200", "404", "500"]

# sample：从序列a中随机抽取n个元素，并将n个元素生以list形式返回
#随机生成用户访问的URL
def sample_url():
    return random.sample(url_path, 1)[0]

# join() 方法用于将序列中的元素以.join()左侧指定的字符连接生成一个新的字符串
#随机生成访问源IP
def sample_ip():
    ip_slice_sample4 = random.sample(ip_slices, 4)
    return ".".join(str(x) for x in ip_slice_sample4)

# uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内。
# 模拟未从搜索引擎跳转的情况，返回-
#随机生成搜索引擎跳转URL
def sample_search():
    if random.uniform(0, 1) > 0.6:
        return "-"

    search_engine_sample = random.sample(search_engine, 1)[0]
    search_keyword_sample = random.sample(search_keyword, 1)[0]
    return search_engine_sample.format(query = search_keyword_sample)

#随机生成HTTP状态码
def sample_status():
    return random.sample(http_status, 1)[0]

# 随机生成日志记录，数量可配置，不输入入参，默认生成10条
def generate_log(count = 10, path="access_log"):
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f = open(path, "w+")
    while count >= 1:
        query_log = "{local_time}\t{url}\t{ip}\t{search_url}\t{http_status}".format(local_time=time_str,url=sample_url(),ip=sample_ip(),search_url=sample_search(),http_status=sample_status())
        print(query_log)
        f.write(query_log+"\n")
        count = count - 1
    f.close()

if __name__ == '__main__':
    generate_log(50)