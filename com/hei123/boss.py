from bs4 import BeautifulSoup
from lxml import html
import requests
from xlwt import *

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'h-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://www.zhipin.com/?sid=sem_pz_bdpc_dasou_title',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
cookies = {
    'Cookie': 'lastCity=101280600; _uab_collina=156213596289177283908984; sid=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1562135963,1562641736; __c=1562641736; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; __a=53721451.1562135963.1562135963.1562641736.35.2.3.3; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1562641749'}
# 新建一个excel文件放在内存中
file = Workbook(encoding='utf-8')
# 给excel文件添加一个sheet页 cell_overwrite_ok设置为false表示禁止重复写入数据
table = file.add_sheet('data', cell_overwrite_ok=False)
# table.write(row_num,col_num,value) 写入数据，往第row_num行，第col_num列写入数据value
table.write(0, 0, u'岗位名称')
table.write(0, 1, u'岗位薪资')
table.write(0, 2, u'公司信息')
table.write(0, 3, u'地址')
table.write(0, 4, u'经验要求')
table.write(0, 5, u'学历要求')

current_row_num = 1  # 写入excel的位置，每次循环后都会加1，方便确认写入excel的哪一行

for i in range(10):
    url = "https://www.zhipin.com/c101280600/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page=" + str(i) + "&ka=page-1"
    f = requests.get(url, headers=headers, cookies=cookies)  # Get该网页从而获取该html内容
    soup = BeautifulSoup(f.text, "lxml")  # 用lxml解析器解析该网页的内容, 好像f.text也是返回的html
    find_all = soup.find_all('div', class_='job-primary')  # 找到div并且class为pl2的标签
    for k in find_all:
        # 找到公司相关信息
        companyInfo = k.find_all('div', class_='info-company')
        # 从公司相关信息中找到公司名称
        companyName = companyInfo[0].find_all("h3")
        # 从公司相关信息中找到公司人数
        companyPeopleNum = companyInfo[0].find_all("p")
        # 找到岗位名称
        title = k.find_all('div', class_='job-title')  # 在每个对应div标签下找span标签，会发现，一个a里面有四组span
        # 找到薪资
        money = k.find_all('span', class_='red')
        # 找到额外相关信息
        extInfo = k.find_all('p')
        # 从额外相关信息中找到地址
        address = extInfo[0].contents[0]
        # 从额外相关信息中找到经验要求
        experience_info = extInfo[0].contents[2]
        # 从额外相关信息中找到学历要求
        graduate_info = extInfo[0].contents[4]
        table.write(current_row_num, 0, title[0].text)
        table.write(current_row_num, 1, money[0].text)
        table.write(current_row_num, 2, companyName[0].text)
        table.write(current_row_num, 3, address)
        table.write(current_row_num, 4, experience_info)
        table.write(current_row_num, 5, graduate_info)
        current_row_num += 1
# 保存文件为data.xls
file.save('data.xls')
