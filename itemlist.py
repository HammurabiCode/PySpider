# -*- coding: utf-8 -*-

import re, urllib, sys

def getHtml(url):
	return urllib.urlopen(url).read()

url = 'http://www.sina.com.cn'
url = 'http://www.taobao.com'
url = 'https://www.qiushibaike.com'
url = 'https://s.taobao.com/search?q=%E7%BA%AF%E6%B0%B4%E6%9C%BA&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160301&cps=yes&ppath=10064123%3A10765672'

html = getHtml(url)
#print html

str1 = r'\"title\":\"(\S*?)\"'
str1 = r'\"title\":\"([^\"]*)\",\"raw_title\"'

title_re = re.compile(str1)

title_list = title_re.findall(html)

#print title_list[0]
print len(title_list)
"""
item1 = title_list[0]
print item1
item1 = item1.decode('utf-8')
print item1
item1 = item1.replace(r'\u003cspan class\u003dH\u003e', '')
print item1
item1 = item1.replace(r'\u003c/span\u003e', '')
print item1
"""
for i in title_list:
    i = i.decode('utf-8')
    i = i.replace(r'\u003cspan class\u003dH\u003e', '')
    i = i.replace(r'\u003c/span\u003e', '')
    print i
    pass
