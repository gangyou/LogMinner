#-*- coding=utf8 -*-
'''
Created on Apr 8, 2013

@author: eric
'''
from copy import copy
from src.main.scanner.LineScanner import LineScanner
class WindowScanner(object):
    '''
    以窗口模式读取文件
    '''
    def __init__(self, size, *filenames):
        self.size= size;
        self.line_scanner = LineScanner(*filenames)
        
    def __iter__(self):
        window = []
        for no, line in enumerate(self.line_scanner):
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
            
            
                
                
            
        