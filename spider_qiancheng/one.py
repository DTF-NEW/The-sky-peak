import re

data = open(r'e:\The-sky-peak\The-sky-peak\spider_qiancheng\a.txt', encoding='utf-8').read()
print(data)
regex = re.compile('c:"([\u4E00-\u9FA5]{1,5}/?[\u4E00-\u9FA5]{1,5}/?[\u4E00-\u9FA5]{1,5}/?[\u4E00-\u9FA5]{1,5}/?).*"Government,Non Profit')
b = re.findall(regex, data)
print(b)
