#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import requests
import csv
import codecs
import xlwt

url_dict = {'unit01': ['https://www.shanbay.com/wordlist/107125/213385/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213385/?page=2'],

            'unit02': ['https://www.shanbay.com/wordlist/107125/213391/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213391/?page=2',
                       'https://www.shanbay.com/wordlist/107125/213391/?page=3'],

            'unit03': ['https://www.shanbay.com/wordlist/107125/213400/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213400/?page=2'],

            'unit04': ['https://www.shanbay.com/wordlist/107125/213403/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213403/?page=2',
                       'https://www.shanbay.com/wordlist/107125/213403/?page=3'],

            'unit05': ['https://www.shanbay.com/wordlist/107125/213409/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213409/?page=2'],

            'unit06': ['https://www.shanbay.com/wordlist/107125/213415/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213415/?page=2',
                       'https://www.shanbay.com/wordlist/107125/213415/?page=3',
                       'https://www.shanbay.com/wordlist/107125/213415/?page=4'],

            'unit07': ['https://www.shanbay.com/wordlist/107125/213424/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213424/?page=2',
                       'https://www.shanbay.com/wordlist/107125/213424/?page=3'],

            'unit08': ['https://www.shanbay.com/wordlist/107125/213460/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213460/?page=2',
                       'https://www.shanbay.com/wordlist/107125/213460/?page=3',
                       'https://www.shanbay.com/wordlist/107125/213460/?page=4',
                       'https://www.shanbay.com/wordlist/107125/213460/?page=5'],

            'unit09': ['https://www.shanbay.com/wordlist/107125/213487/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213487/?page=2',
                       'https://www.shanbay.com/wordlist/107125/213487/?page=3'],

            'unit10': ['https://www.shanbay.com/wordlist/107125/213490/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213490/?page=2',
                       'https://www.shanbay.com/wordlist/107125/213490/?page=3',
                       'https://www.shanbay.com/wordlist/107125/213490/?page=4'],

            'unit11': ['https://www.shanbay.com/wordlist/107125/213493/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213493/?page=2'],

            'unit12': ['https://www.shanbay.com/wordlist/107125/213517/?page=1',
                       'https://www.shanbay.com/wordlist/107125/213517/?page=2']
            }


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
    # get the contents in source page
    # src_content = check_link(src_url)

    # get all the useful urls in source page
    # urls = get_urls(src_content)

    # scrapy all the useful contents from all the urls

    for unit_info, url_list in url_dict.items():
        result = get_contents(url_list)
        write_sheet(unit_info, result)

    save_xls('newnewnewnew.xls')

main()

