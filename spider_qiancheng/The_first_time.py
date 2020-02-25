# 本次爬虫为获取职业方向而爬取
import requests
import urllib.request
from fake_useragent import UserAgent  # 随机请求头第三方库
import re

# 创建请求变量，应对反爬第一道防线
from parsel.xpathfuncs import regex

url = "https://search.51job.com/jobsearch/advance_search.php"
url_02 = "https://js.51jobcdn.com/in/resource/js/2020/search/common.fa18f498.js"
test_url = "http://httpbin.org/get"
# 定义请求头
ua = UserAgent()
try:
    head = {"User-Agent": ua.random}
except Exception:
    print("已达到最大重试次数")


# 第一种得到响应对象的方式
def one_html(one_url):
    pack_url = urllib.request.Request(url=one_url, headers=head)  # 包装请求头
    one_response = urllib.request.urlopen(pack_url)  # urllib.request获取响应内容
    html_result = one_response.read().decode('gbk')  # 读取内容转换格式
    return html_result


# 第二种得到响应内容的方式
def two_html(two_url):
    html_result = requests.get(two_url, headers=head)
    html_result.encoding = 'gbk'
    return html_result.text


html = requests.get(url_02).text
print(html)
b = re.findall('', html)
print(b)
