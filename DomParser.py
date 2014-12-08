#coding:utf-8
'''
Created on 2014-4-9

@author: nice
'''
from xml.dom import minidom
import codecs

class ItemParserHelper(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.filename = params;
        
    def loadXmlAsString(self):
        f = codecs.open(self.filename, 'rb')
        self.text = f.read()
        f.close()
        return self.text
    
    def xmlParser(self, name):
        #doc = minidom.parseString(self.loadXmlAsString())
        doc = minidom.parse(self.filename)
        root = doc.documentElement
        nodelist = self.get_XmlNode(root, name)
        for node in nodelist:
            print self.get_NodeText(node.childNodes)
        
       
            
        
        
    
    def get_XmlNode(self, node, name):
        if node:
            return node.getElementsByTagName(name)
        else:
            return []
        
    def get_NodeText(self, nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return rc
  
    def get_AttrValue(self, node, name):
        """
        get attribute of one node
        """
        if node:
            return node.getAttribute(name)
        else:
            return ''
        
        