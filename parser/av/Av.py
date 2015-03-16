#encoding:utf-8
'''
Created on Mar 12, 2015

@author: root
'''

class av(object):
    id=""
    name=""
    publicdate=""
    duration=""
    actors=""
    category=""
    img=""
    html=""
    
    def __init__(self,id,name,publicdate,duration,actors,category,img,html):
        self.id = id
        self.name = name
        self.publicdate = publicdate
        self.duration = duration
        self.actors = actors
        self.category = category
        self.img = img
        self.html = html
        
    def tosql(self):
        sql = "Insert into ebook(id,name,publicdate,duration,actors,category,img,html) VALUES (?,?,?,?,?,?,?)"
#         print sql
        return sql
        