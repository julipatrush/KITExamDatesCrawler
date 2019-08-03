# -*- coding: utf-8 -*-
from collections import OrderedDict
import scrapy
import types

def addToSQL(examName, examTime, examDate):
    print("ggg")


class KitInfoExamsSpider(scrapy.Spider):
    name = 'kit_info_exams'
    allowed_domains = ['www.informatik.kit.edu/9581.php']
    start_urls = ['https://www.informatik.kit.edu/9581.php/']

    def parse(self, response):
        #Extracting the content using css selectors
        products = response.css('a[name=block10240] + table tr')
        for p in products:
            #exam = dict()
            #exam['examName'] = p.css('td:nth-child(1) a::text').extract_first()
            #exam['examTime'] = p.css('td:nth-child(2)::text').extract_first()
            #exam['examDate'] = p.css('td:nth-child(3)::text').extract_first()
            examName = p.css('td:nth-child(1) a::text').extract_first()
            examDate = p.css('td:nth-child(2)::text').extract_first()
            examTime = p.css('td:nth-child(3)::text').extract_first()

            sql_file = open('kit_exams_ss19.sql', 'a')
            exam_dates_day = []
            exam_dates_month = []
            exam_dates_year=[]
            exam_startTimes_hours = []
            exam_startTimes_minutes = []
            exam_startTimes_sec = []
            NoneType = type(None)
            if type(examName) != NoneType:
                try:
                    exam_startTimes_hours, exam_startTimes_minutes = examTime.split(":")
                    exam_startTimes_sec = 0;
                except:
                    exam_startTimes_hours = 0
                    exam_startTimes_minutes = 0
                    exam_startTimes_sec = 0
                try:
                    exam_dates_day, exam_dates_month, exam_dates_year = examDate.split(".")
                except:
                    exam_dates_day = 0
                    exam_dates_month = 0
                    exam_dates_year = 0
                print(examName)
                string = "INSERT INTO timers VALUES ('{}','Viel Erfolg!',{},{},{},{},{},{});\n".format(examName.encode("utf-8"), exam_dates_day, exam_dates_month, exam_dates_year, exam_startTimes_hours, exam_startTimes_minutes, exam_startTimes_sec)
                sql_file.write(string)
        sql_file.close()
