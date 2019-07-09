#!/usr/bin/env python
# coding=utf-8

from xlwt import *

# 需要xlwt库的支持
# import xlwt
file = Workbook(encoding='utf-8')
# 指定file以utf-8的格式打开
table = file.add_sheet('data')
# 指定打开的文件名

data = {
    "1": ["张三", 150, 120, 100],
    "2": ["李四", 90, 99, 95],
    "3": ["王五", 60, 66, 68]
}

table.write(0, 0, u'企业名称')  # 往sheet里第一行第一列写一个数据
table.write(0, 1, u'企业注册号')  # 往sheet里第二行第一列写一个数据

file.save('data.xls')
