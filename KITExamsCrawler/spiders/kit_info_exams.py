# -*- coding: utf-8 -*-
from collections import OrderedDict
import scrapy


class KitInfoExamsSpider(scrapy.Spider):
    name = 'kit_info_exams'
    allowed_domains = ['www.informatik.kit.edu/9581.php']
    start_urls = ['https://www.informatik.kit.edu/9581.php/']

    def parse(self, response):
        #Extracting the content using css selectors
        exam_titles = response.css('td a::text').extract()
        exam_date = response.css('td::text').extract()
        exam_dates_day = []
        exam_dates_month = []
        exam_dates_year=[]
        exam_startTimes_hours = []
        exam_startTimes_minutes = []
        exam_startTimes_sec = []
        for x in exam_date:
            if (len(x) == 5):
                hours, minutes = x.split(":")
                exam_startTimes_hours.append(hours)
                exam_startTimes_minutes.append(minutes)
                exam_startTimes_sec.append(0);
            elif (len(x) >7):
                day, month, year = x.split(".")
                exam_dates_day.append(day)
                exam_dates_month.append(month)
                exam_dates_year.append(year)

        exams = OrderedDict()
        for item in zip(exam_titles, exam_dates_day, exam_dates_month, exam_dates_year, exam_startTimes_hours, exam_startTimes_minutes, exam_startTimes_sec):
            exams = {
                1 : item[0],
                2 : 'Viel Erfolg!',
                3  : item[1],
                4  : item[2],
                5   : item[3],
                6   : item[4],
                7   : item[5],
                8   : item[6],
            }

            yield exams
