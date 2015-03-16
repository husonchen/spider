#encoding:utf-8
'''
Created on Mar 11, 2015
解析展示表页面
@author: root
'''
from bs4 import BeautifulSoup  
import spider.WebPageSpider
from spider import WebPageSpider
import parser.BaseParser
from parser.BaseParser import tag_children
from parser.book.Book import ebook

def parse(html):
    soup = BeautifulSoup(html)
    trs = tag_children(soup.table)
#     print trs.contents[3]
    for i in range(1,len(trs)):
        tds = tag_children(trs[i])
#         print tds[0]
        book = ebook(tds[1].a.text,tds[2].text,tds[3].text,tds[4].text,tds[5].text,tds[6].text,tds[0].a.text,tds[7].a.attrs['href'])
        book.tosql()
        
    
    
if __name__ == '__main__':
    html = WebPageSpider.getBoardHtml(1)
    parse(html)