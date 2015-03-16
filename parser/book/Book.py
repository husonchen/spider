#encoding:utf-8
'''
Created on Mar 12, 2015

@author: root
'''

class ebook(object):
    name=""
    anthor=""
    pubtime=""
    page=""
    ISBN=""
    size=""
    form="PDF"
    link="ed2k://"
    
    def __init__(self,name,anthor,pubtime,page,ISBN,size,form,link):
        self.name = name
        self.anthor = anthor
        self.pubtime = pubtime
        self.page = page
        self.ISBN = ISBN
        self.size = size
        self.form = form
        self.link = link
        
    def tosql(self):
        sql = "Insert into ebook(name,anthor,pubtime,page,ISBN,size,form,link) VALUES ('"+\
        self.name+"','"+self.anthor+"','"+self.pubtime+"','"+self.page+"','"+self.ISBN+"','"+self.size+"','"+\
        self.form+"','"+self.link+"')"
        print sql
        return sql
        