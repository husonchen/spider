#encoding:utf-8
'''
Created on 2015年3月14日

@author: Mac
'''
from bs4 import BeautifulSoup  
from spider import WebPageSpider
from parser.BaseParser import tag_children
import string
from Av import av
from spider.WebPageSpider import getHtml
import sys
from repository import AvRepository
import socket

def parse(html,repository):
    soup = BeautifulSoup(html)
    trs = tag_children(soup.find(id="og-grid"))
#     print trs.contents[3]
    for i in range(1,len(trs)):
        try:
            tds = tag_children(trs[i])
            brs = tds[0]["data-description"].replace("\n","").replace("\t","").split("<br>")
    #         print brs[0][8:-9]
            html = ""
            try:
                html = getHtml("http://bt8.nl/"+tds[0]["href"])
            except Exception,e:
                file_object = open('error.txt', 'w')
                file_object.write("http://bt8.nl/"+tds[0]["href"]+"\n\r")
                file_object.close()
            v = av(brs[1],brs[0][8:-9],brs[2],brs[3],brs[8],brs[7],tds[0]["data-largesrc"],html.decode("UTF-8"))
            repository.saveDB(v)
        except Exception,e:
            print e
        
        
        
    
    
if __name__ == '__main__':
    
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    
    socket.setdefaulttimeout(10.0)
    repository = AvRepository.AvRepository()
    for i in range(1,819):
        print i
        try:
            html = WebPageSpider.getAvHtml(i)
            parse(html,repository)
        except Exception,e:
            print e