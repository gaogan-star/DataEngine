# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import xlwt


pages = int(input())
urls = []
complaint_all = []


def get_complaint(url, i_url):
    cpt_all_out = []
    res = urllib.request.urlopen(url)
    soup = (BeautifulSoup(res, "html.parser"))
    cpt_content = soup.find('table', attrs={'class': 'ar_c ar_c1'})
    tr_item = cpt_content.findAll('tr')
    for item in tr_item:
        temp = []
        th_item = item.findAll('th')
        td_item = item.findAll('td')
        if (len(th_item) > 0) & (i_url < 1):
            for i in range(len(th_item)):
                temp.append(th_item[i].get_text())
        if len(td_item) > 0:
            for i in range(len(td_item)):
                temp.append(td_item[i].get_text())
        cpt_all_out.append(temp)
    return cpt_all_out


def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)   # 创建sheet
    i = 0
    for data in datas:
        i = i + 1
        for j in range(len(data)):
            print(data[j])
            sheet1.write(i, j, data[j])
    f.save(file_path)     # 保存文件


if pages > 0:
    for page in range(1, pages + 1):
        url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-' + str(page) + '.shtml'
        urls.append(url)
for i in range(len(urls)):
    complaint_all += get_complaint(urls[i], i)
file_path = r'D:\11_Bigdata\黑马数据大赛培训\day2\test.xls'
data_write(file_path, complaint_all)
print(complaint_all)

