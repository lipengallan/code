#!/usr/bin/env python
#coding:utf-8

import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import requests
import csv
import codecs
import xlwt
#from word_power_dict import get_url_dict
#from Vocabulary_Toefl_MP3s_5000_Words_Memory_Course_dict import get_url_dict
#from new_parade_1_dict import get_url_dict
#from new_parade_1_dict import name as xlsname

#from new_parade_2.new_parade_2_dict import get_url_dict
#from new_parade_2.new_parade_2_dict import name as xlsname


#from new_parade_3.new_parade_3_dict import get_url_dict
#from new_parade_3.new_parade_3_dict import name as xlsname


from new_parade_4.new_parade_4_dict import get_url_dict
from new_parade_4.new_parade_4_dict import name as xlsname

def check_link(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print '----------'
        print e
        print '----------'


def is_alphabet(uchar):
    if (u'\u0041' <= uchar <= u'\u005a') or (u'\u0061' <= uchar <= u'\u007a'):
        return True
    else:
        return False


def save_contents(result):
    '''result: all the useful result from urls'''
    with codecs.open('merriam.csv', 'w', 'utf_8_sig') as f:
        writer = csv.writer(f)
        for i in range(len(result)):
            try:
                if is_alphabet(result[i][1][0]):
                    writer.writerow([result[i][1], result[i][3]])
                    print("write in line:", i)
            except:
                print("error in line:{}, contents is:{}".format(i, result[i]))


workbook = xlwt.Workbook(encoding='utf-8')

ENGLISH_WORD, CHINESE_TRANSLATE = (0, 1)


def write_sheet(unit_info, result):
    sheet = workbook.add_sheet(unit_info, cell_overwrite_ok=True)
    begin_row = 0
    for i in range(len(result)):
        try:
            if is_alphabet(result[i][1][0]):
                sheet.write(begin_row, ENGLISH_WORD, label=result[i][1])
                sheet.write(begin_row, CHINESE_TRANSLATE, label=result[i][3])
                print("write in line:", i)
                begin_row += 1
        except:
            print("error in line:{}, contents is:{}".format(i, result[i]))




def save_xls(name):
    workbook.save(name)


def get_contents(urls):
    result = []
    for one_url in urls:
        content = check_link(one_url)
        soup = BeautifulSoup(content, 'lxml')
        trs = soup.find_all('tr')
        for tr in trs:
            ui = []
            for td in tr:
                ui.append(td.string)
            result.append(ui)
        time.sleep(1)
    return result


'''
def get_urls(url_content, root_url="https://www.shanbay.com"):    
    ulist = []
    soup = BeautifulSoup(url_content, 'lxml')
    urls = soup.find_all('a')
    for url in urls:
        try:
            if url.string.startswith('【无老师7天TOEFL】List'):
                ulist.append(root_url + url.get('href'))
                for j in range(2, 11):
                    extend_url = root_url + url.get('href') + '?page=' + str(j)
                    ulist.append(extend_url)
        except:
            pass
    return ulist
'''


def main():
    test_url = 'https://www.shanbay.com/wordlist/107125/213385/?page=1'
    url_dict = get_url_dict()
    for unit_info, url_list in url_dict.items():
        result = get_contents(url_list)
        write_sheet(unit_info, result)

    save_xls(xlsname+'.xls')




main()

