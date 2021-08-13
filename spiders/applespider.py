# -*- coding: utf-8 -*-

import scrapy
import csv
from datetime import date


class financeapple(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['yahoo.com/']
    start_urls = ['https://finance.yahoo.com/quote/AAPL?p=AAPL']
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'test.csv'
    }
    
    def parse(self,response):
        
        for info in response.xpath('//div[@id="quote-summary"]'):
            temp = dict()
            temp['Title']=response.xpath('//div[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1/text()').extract()
            temp['Previous_Close'] = info.xpath('.//div[1]/table/tbody/tr[1]/td[2]/span/text()').extract()
            temp['Market_Cap'] = info.xpath('.//div[2]/table/tbody/tr[1]/td[2]/span/text()').extract()
            temp['Open'] = info.xpath('.//div[1]/table/tbody/tr[2]/td[2]/span/text()').extract()
            temp['Beta_5Y_Monthly'] = info.xpath('.//div[2]/table/tbody/tr[2]/td[2]/span/text()').extract()
            temp['Bid'] = info.xpath('.//div[1]/table/tbody/tr[3]/td[2]/span/text()').extract()
            temp['PE_Ratio_TM'] = info.xpath('.//div[2]/table/tbody/tr[3]/td[2]/span/text()').extract() 
            temp['Ask'] = info.xpath('.//div[1]/table/tbody/tr[4]/td[2]/span/text()').extract()
            temp['EPS_TTM'] = info.xpath('.//div[2]/table/tbody/tr[4]/td[2]/span/text()').extract()
            temp['Days_Range'] = info.xpath('.//div[1]/table/tbody/tr[5]/td[2]/text()').extract()
            temp['Earning_Date'] = info.xpath('.//div[2]/table/tbody/tr[5]/td[2]/span/text()').extract()
            temp['52Week_Range'] = info.xpath('.//div[1]/table/tbody/tr[6]/td[2]/text()').extract()
            temp['Forward_Dividend_&_Yield'] = info.xpath('.//div[2]/table/tbody/tr[6]/td[2]/text()').extract()
            temp['Volume'] = info.xpath('.//div[1]/table/tbody/tr[7]/td[2]/span/text()').extract()
            temp['Ex-Dividend_Date'] = info.xpath('.//div[2]/table/tbody/tr[7]/td[2]/span/text()').extract()
            temp['Avg_Volume'] = info.xpath('.//div[1]/table/tbody/tr[8]/td[2]/span/text()').extract()
            temp['1y_Target_Est'] = info.xpath('.//div[2]/table/tbody/tr[8]/td[2]/span/text()').extract()
            temp['date'] = date.today()
            yield temp
