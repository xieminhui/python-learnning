"""
@Date: 2020-01-07 11:03:03
@LastEditors: xieminhui
@LastEditTime: 2020-01-07 11:03:14
"""
import urllib.request

url = "http://www.baidu.com"
response1 = urllib.request.urlopen(url)
# 获取状态码，200表示成功
print(response1.getcode())
# 获取网页内容的长度

with open("baidu.html", "wb") as f:
    f.write(response1.read())
