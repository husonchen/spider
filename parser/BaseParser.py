#encoding:utf-8
'''
Created on Mar 11, 2015

@author: root
'''
from bs4 import BeautifulSoup 
from bs4 import element

def right_tag(tag,name=None):  
    if not name or tag.name == name:  
        return tag  
  
def tag_children(tag,name=None):  
    """ 
    找到所有类型为标签的子元素,可通过name参数指定标签种类. 
    """  
    children = []  
    contents = tag.contents  
    for content in contents:  
        if isinstance(content,element.Tag):  
            child = right_tag(content,name)  
            if child:  
                children.append(child)  
    return children  

if __name__ == '__main__':
    pass