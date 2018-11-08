#!/usr/bin/env python
#coding:utf-8

import xlrd
import os
import urllib2
import time

src_file = './Vocabulary_Toefl_MP3s_5000_Words_Memory_Course/5000_Words.xls'
base_mp3_url = 'http://media.shanbay.com/audio/us/%s.mp3'
MP3_DIR = src_file.replace('.xls','_mp3')
FAILED_LOG = src_file.replace('xls','log')

wb = xlrd.open_workbook(src_file)
sheets_list = wb.sheets()


def write_log(content):
    with open(FAILED_LOG, 'a+') as f:
        f.write(content)



def get_url_dict():
    mp3_url_dict = {}
    for sheet in sheets_list:
        mp3_url_list = []
        name = sheet.name
        print name
        sheet_content = wb.sheet_by_name(name)
        words = sheet_content.col_values(0)
        for word in words:
            url = base_mp3_url % word
            mp3_url_list.append(url)
        mp3_url_dict[name] = mp3_url_list
    return mp3_url_dict


def download_mp3(mp3_url_dict):
    for name, url_list in mp3_url_dict.items():
        mp3_download_dir = os.path.join(MP3_DIR, name)

        if not os.path.exists(mp3_download_dir):
            os.makedirs(mp3_download_dir)

        for url in url_list:
            mp3_name = url.split('/')[-1].lower()
            mp3_full_name = os.path.join(mp3_download_dir, mp3_name)

            if os.path.exists(mp3_full_name):
                continue

            try:
                req2 = urllib2.Request(url)
                response = urllib2.urlopen(req2)
                #grab the data
                data = response.read()
            except urllib2.HTTPError:
                write_log(mp3_full_name + '\n')
                continue



            with open(mp3_full_name, "wb") as f:
                f.write(data)    # was data2
            #time.sleep(1)


def main():
    mp3_url_dict = get_url_dict()
    download_mp3(mp3_url_dict)

if __name__ == '__main__':
    if os.path.exists(FAILED_LOG):
        os.unlink(FAILED_LOG)
    main()
