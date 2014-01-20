#!/usr/bin/env python
#_*_ coding:utf8 _*_
'''
@author:    damonhu
@date:      2014/01/20 first build
@purpose:   After reload svr, read log to alter error
'''

import os
import time
import re

pattern = re.compile(r'(?<=\[).*?(?=\])', re.DOTALL)

#after reload svr, read log
def readLog(filename, nowtime):
    flag = False
    f = open(filename, 'r')
    for line in f:
        match = pattern.search(line)
        if match:
            timestr = match.group(0).split('.')[0]
            logtime = time.mktime(time.strptime(timestr, '%Y%m%d %H:%M:%S'))
            if logtime > nowtime and 'error' in line:
                print 'There is an error after reload svr!'
                flag = True
    f.close()
    return flag

def svrList():
    nowtime = time.time()
    f = open(r'monitor.log', 'r')
    for filename in f:
        filename = filename.strip('\n')
        print filename
        if readLog(filename, nowtime):
            break
        else:
            print 'read svr success!'
    f.close()

def errorLogList(path):
    for root, dirname, filename in os.walk(path):
        if 

if __name__ == '__main__':
    svrList()
