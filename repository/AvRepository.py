#encoding:utf-8
'''
Created on 2015年3月17日

@author: Mac
'''
import MySQLdb

class AvRepository:
    conn=MySQLdb.connect(host='121.42.44.146',user='btestuser',passwd='AOED2&D',db='blogtest',port=3306,charset="utf8")
    cur=conn.cursor()

    def saveDB(self,av):
        self.cur.execute("Insert into av(id,name,publicdate,duration,actors,category,img,html) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"\
                         ,(av.id,av.name,av.publicdate,av.duration,av.actors,av.category,av.img,av.html))
        self.conn.commit()
        
#         count=self.cur.execute('select * from av')
#         print 'there has %s rows record' % count
#      
#         result=self.cur.fetchone()
#         print result[7]

if __name__ == '__main__':
    pass