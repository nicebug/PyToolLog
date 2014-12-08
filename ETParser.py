#coding:utf-8
'''
Created on 2014-4-9

@author: nice
'''

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
#import ConfigParser
import re

########################################################################
class ETParserHelperWithIter:
    """
    parser xml with iterparse() 
    """

    #----------------------------------------------------------------------
    def __init__(self, filename):
        """Constructor"""
        #self.context = ET.iterparse(filename)
        self.tree = ET.ElementTree(file=filename)
    
    #----------------------------------------------------------------------
    def ETParser(self, node, itemid, itemname):
        """
        parse xml
        """
        result = {}
        start = False
        for event, elem in self.context:
            if event == 'end':
                ids = ''
                name = ''
                if elem.tag == node :
                    for elem_child in ET.iter(elem.tag):
                        print elem_child.tag, elem_child.text
            elem.clear()
        return result
                    
        
      
        
    
    


class ETParserHelper(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.filename = params

    def ETParser(self, node, itemid, itemname):
        """
        @param node: xml node, Supported XPath syntax
        @param itemid: ItemID node
        @param itemname: ItemName node
        @return: map of id and name
        """
        result = {}
        tree = ET.parse(self.filename)
        root = tree.getroot()

        for item in root.findall(node):
            ids = item.find(itemid).text.strip()
            name = item.find(itemname).text
            result[ids] = name
        return result

    def ETParserID(self, node, itemid):
        result = []
        tree = ET.parse(self.filename)
        root = tree.getroot()
        for item in root.findall(node):
            ids = item.find(itemid).text.strip()
            result.append(ids)
        return result


class UDKAvatarHelper(object):
    '''
    pick out all id in ini file
    '''
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename)
        self.parttern = re.compile(r"\((.*)\)")
    
    def parser(self):
        avatarid = set()
        for line in self.f:
            if "NPCSoundConfigs" in line or "NPCResItemConfigs" in line:
                continue
            if "Id" in line:
                result = self.parttern.findall(line)[0].strip("Id=")
                avatarid.add(result.split(",")[0].strip())
        self.f.close()
        return avatarid
'''
#comment the code for test
class UDKAvatarParerHelper(object):
    def __init__(self, parms):
        self.filename = parms
        self.config = ConfigParser.ConfigParser()
        #self.config.read(self.filename)

    def UDKAvatarParser(self):
        section_list = self.config.sections()
        for se in section_list:
            print se
            options = self.config.options(se)
            for option in options:
                print option
            #print self.getSectionMap(se)
            break


    def getSectionMap(self, section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = section.config.get(section, option)
                if dict1[option] == -1:
                    print 'error'
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
'''

