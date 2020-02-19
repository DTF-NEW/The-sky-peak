# 本次爬虫为获取职业方向而爬取
# UTF-8
import requests
from fake_useragent import UserAgent
import time

# 创建请求变量，应对反爬第一道防线
# 定义请求URL
url = "https://search.51job.com/jobsearch/advance_search.php"
url_test = "http://httpbin.org/get"
# 定义请求头
ua = UserAgent()
head = {"User-Agent": ua.random}
# try:
#     head = {"User-Agent": ua.random}
# except Exception:
#     print("已达到最大重试次数")
# # 包装请求对象
# url_defined = urllib.request.Request(url=url_test, headers=head)
# # 得到响应对象
# qiancheng = urllib.request.urlopen(url_test)
# 获取响应内容
qc_html = requests.get(url_test, headers=head)
get_code = qc_html.text
print(get_code)
