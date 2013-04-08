#-*- coding=utf8 -*-
'''
Created on Apr 8, 2013

@author: eric
'''
from copy import copy
class WindowScanner(object):
    '''
    以窗口模式读取文件
    '''
    def __init__(self, filename, size):
        self.filename = filename;
        self.size= size;
        
    def __iter__(self):
        window = []
        with open(self.filename) as f:
            for no, line in enumerate(f):
                if no < self.size:
                    window.append(line)
                    continue
                elif no == self.size:
                    first_block = copy(window)
                    window = self.__shift_and_append(window, line)
                    yield "".join(first_block)
                else:
                    window = self.__shift_and_append(window, line)
                    yield "".join(window)
                    
    
    def __shift_and_append(self, window, line):
        window = window[1:]
        window.append(line)
        return window
            
            
                
                
            
        