#encoding:utf-8
'''
Created on Mar 11, 2015

@author: root
'''
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getBoardHtml(page):
    return getHtml("http://bt8.nl/ebook.php?page="+str(page)+"&type=&book=")

if __name__ == '__main__':
    getBoardHtml(1)