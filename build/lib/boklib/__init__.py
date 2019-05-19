#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as ET

def opendata(url):
    html = requests.get(url)
    xml = ET.fromstring(html.text)
    return xml

class bok:
    def __init__(self, key, lang):
        self.key = key
        self.lang = lang

    def key_List(self, start_count = 1, end_count = 100000):
        self.start_count = start_count
        self.end_count = end_count
        self.url = 'http://ecos.bok.or.kr/api/KeyStatisticList/' + self.key + '/xml/' + self.lang + '/' + str(self.start_count) + '/' + str(self.end_count)
        self.data = opendata(self.url)
        if self.data is None:
            return {'CODE' : 'CODE-0', 'MESSAGE' : 'none data'}
        elif self.data.tag == 'RESULT':
            self.code = self.data[0].text
            self.message = self.data[1].text
            err = {'CODE' : self.code, 'MESSAGE' : self.message}
            return err
        else:
            self.stat_result = {'list_total_count' : {}, 'row' : []}
            for i in range(len(self.data)):
                if i == 0:
                    self.list_total_count = self.data[0].text
                    self.stat_result['list_total_count'] = self.list_total_count
                else:
                    self.class_name = self.data[i][0].text
                    self.keystat_name = self.data[i][1].text
                    self.data_value = self.data[i][2].text
                    self.cycle = self.data[i][3].text
                    self.unit_name = self.data[i][4].text
                    self.stat_result['row'] += [{'CLASS_NAME' : self.class_name, 'KEYSTAT_NAME' : self.keystat_name, 'DATA_VALUE' : self.data_value, 'CYCLE' : self.cycle, 'UNIT_NAME' : self.unit_name}]
            return self.stat_result

    def table_list(self, start_count = 1, end_count = 100000):
        self.start_count = start_count
        self.end_count = end_count
        self.url = 'http://ecos.bok.or.kr/api/StatisticTableList/' + self.key + '/xml/' + self.lang + '/' + str(self.start_count) + '/' + str(self.end_count)
        self.data = opendata(self.url)
        if self.data is None:
            return {'CODE' : 'CODE-0', 'MESSAGE' : 'none data'}
        elif self.data.tag == 'RESULT':
            self.code = self.data[0].text
            self.message = self.data[1].text
            err = {'CODE' : self.code, 'MESSAGE' : self.message}
            return err
        else:
            self.stat_result = {'list_total_count' : {}, 'row' : []}
            for i in range(len(self.data)):
                if i == 0:
                    self.list_total_count = self.data[0].text
                    self.stat_result['list_total_count'] = self.list_total_count
                else:
                    self.p_stat_code = self.data[i][0].text
                    self.stat_code = self.data[i][1].text
                    self.stat_name = self.data[i][2].text
                    self.cycle = self.data[i][3].text
                    self.srch_yn = self.data[i][4].text
                    self.org_name = self.data[i][5].text
                    self.stat_result['row'] += [{'P_STAT_CODE' : self.p_stat_code, 'STAT_CODE' : self.stat_code, 'STAT_NAME' : self.stat_name, 'CYCLE' : self.cycle, 'SRCH_YN' : self.srch_yn, 'ORG_NAME' : self.org_name}]
            return self.stat_result

    def item_list(self, stat_code, start_count = 1, end_count = 100000):
        self.start_count = start_count
        self.end_count = end_count
        self.stat_code = stat_code
        self.url = 'http://ecos.bok.or.kr/api/StatisticItemList/' + self.key + '/xml/' + self.lang + '/' + str(self.start_count) + '/' + str(self.end_count) + '/' + self.stat_code
        self.data = opendata(self.url)
        if self.data is None:
            return {'CODE' : 'CODE-0', 'MESSAGE' : 'none data'}
        elif self.data.tag == 'RESULT':
            self.code = self.data[0].text
            self.message = self.data[1].text
            err = {'CODE' : self.code, 'MESSAGE' : self.message}
            return err
        else:
            self.stat_result = {'list_total_count' : {}, 'row' : []}
            for i in range(len(self.data)):
                if i == 0:
                    self.list_total_count = self.data[0].text
                    self.stat_result['list_total_count'] = self.list_total_count
                else:
                    self.stat_code = self.data[i][0].text
                    self.stat_name = self.data[i][1].text
                    self.grp_code = self.data[i][2].text
                    self.grp_name = self.data[i][3].text
                    self.p_item_code = self.data[i][4].text
                    self.item_code = self.data[i][5].text
                    self.item_name = self.data[i][6].text
                    self.cycle = self.data[i][7].text
                    self.start_time = self.data[i][8].text
                    self.end_time = self.data[i][9].text
                    self.data_cnt = self.data[i][10].text
                    self.stat_result['row'] += [{'STAT_CODE' : self.stat_code, 'STAT_NAME' : self.stat_name, 'GRP_CODE' : self.grp_code, 'GRP_NAME' : self.grp_name, 'P_ITEM_CODE' : self.p_item_code, 'ITEM_CODE' : self.item_code, 'ITEM_NAME' : self.item_name, 'CYCLE' : self.cycle, 'START_TIME' : self.start_time, 'END_TIME' : self.end_time, 'DATA_CNT' : self.data_cnt}]
            return self.stat_result

    def search(self, stat_code, cycle, start_date, end_date, item_code, start_count = 1, end_count = 100000):
        self.start_count = start_count
        self.end_count = end_count
        self.stat_code = stat_code
        self.cycle = cycle
        self.start_date = start_date
        self.end_date = end_date
        self.item_code = item_code
        self.url = 'http://ecos.bok.or.kr/api/StatisticSearch/' + self.key + '/xml/' + self.lang + '/' + str(self.start_count) + '/' + str(self.end_count) + '/' + self.stat_code + '/' + self.cycle + '/' + self.start_date + '/' + self.end_date + '/' + self.item_code
        self.data = opendata(self.url)
        if self.data is None:
            return {'CODE' : 'CODE-0', 'MESSAGE' : 'none data'}
        elif self.data.tag == 'RESULT':
            self.code = self.data[0].text
            self.message = self.data[1].text
            err = {'CODE' : self.code, 'MESSAGE' : self.message}
            return err
        else:
            self.stat_result = {'list_total_count' : {}, 'row' : []}
            for i in range(len(self.data)):
                if i == 0:
                    self.list_total_count = self.data[0].text
                    self.stat_result['list_total_count'] = self.list_total_count
                else:
                    self.stat_code = self.data[i][0].text
                    self.stat_name = self.data[i][1].text
                    self.item_code1 = self.data[i][2].text
                    self.item_name1 = self.data[i][3].text
                    self.item_code2 = self.data[i][4].text
                    self.item_name2 = self.data[i][5].text
                    self.item_code3 = self.data[i][6].text
                    self.item_name3 = self.data[i][7].text
                    self.unit_name = self.data[i][8].text
                    self.time = self.data[i][9].text
                    self.data_value = self.data[i][10].text
                    self.stat_result['row'] += [{'STAT_CODE' : self.stat_code, 'STAT_NAME' : self.stat_name, 'ITEM_CODE1' : self.item_code1, 'ITEM_CODE2' : self.item_code2, 'ITEM_CODE3' : self.item_code3, 'UNIT_NAME' : self.unit_name, 'TIME' : self.time, 'DATA_VALUE' : self.data_value}]
            return self.stat_result

    def meta(self, meta_word, start_count = 1, end_count = 100000):
        self.start_count = start_count
        self.end_count = end_count
        self.meta_word = meta_word
        self.url = 'http://ecos.bok.or.kr/api/StatisticMeta/' + self.key + '/xml/' + self.lang + '/' + str(self.start_count) + '/' + str(self.end_count) + '/' + self.meta_word
        self.data = opendata(self.url)
        if self.data is None:
            return {'CODE' : 'CODE-0', 'MESSAGE' : 'none data'}
        elif self.data.tag == 'RESULT':
            self.code = self.data[0].text
            self.message = self.data[1].text
            err = {'CODE' : self.code, 'MESSAGE' : self.message}
            return err
        else:
            self.stat_result = {'list_total_count' : {}, 'row' : []}
            for i in range(len(self.data)):
                if i == 0:
                    self.list_total_count = self.data[0].text
                    self.stat_result['list_total_count'] = self.list_total_count
                else:
                    self.lvl = self.data[i][0].text
                    self.p_cont_code = self.data[i][1].text
                    self.cont_code = self.data[i][2].text
                    self.cont_name = self.data[i][3].text
                    self.meta_data = self.data[i][4].text
                    self.stat_result['row'] += [{'LVL' : self.lvl, 'P_CONT_CODE' : self.p_cont_code, 'CONT_CODE' : self.cont_code, 'CONT_NAME' : self.cont_name, 'META_DATA' : self.meta_data}]
            return self.stat_result

    def word(self, search_word, start_count = 1, end_count = 100000):
        self.start_count = start_count
        self.end_count = end_count
        self.search_word = search_word
        self.url = 'http://ecos.bok.or.kr/api/StatisticWord/' + self.key + '/xml/' + self.lang + '/' + str(self.start_count) + '/' + str(self.end_count) + '/' + self.search_word
        self.data = opendata(self.url)
        if self.data is None:
            return {'CODE' : 'CODE-0', 'MESSAGE' : 'none data'}
        elif self.data.tag == 'RESULT':
            self.code = self.data[0].text
            self.message = self.data[1].text
            err = {'CODE' : self.code, 'MESSAGE' : self.message}
            return err
        else:
            self.stat_result = {'list_total_count' : {}, 'row' : []}
            for i in range(len(self.data)):
                if i == 0:
                    self.list_total_count = self.data[0].text
                    self.stat_result['list_total_count'] = self.list_total_count
                else:
                    self.word = self.data[i][0].text
                    self.content = self.data[i][1].text
                    self.stat_result['row'] += [{'WORD' : self.word, 'CONTENT' : self.content}]
            return self.stat_result
