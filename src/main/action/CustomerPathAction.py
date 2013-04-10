# -*- coding=utf8 -*-
'''
Created on Apr 9, 2013

@author: eric
'''
from src.main.scanner.WindowScanner import WindowScanner

class CustomerPathAction(object):
    def __init__(self, handler, dest_file, *filenames):
        '''
            @param handler: 行处理句柄
            @param dest_file: 输出文件
            @param *filenames: 待处理文件 
        '''
        self.handler = handler
        self.dest_file = dest_file
        self.filenames = filenames
        
    def action(self, output_format=None):
        scanner = WindowScanner(10, *self.filenames)
        out = open(self.dest_file, 'w')
        count =0 
        for window in scanner:
            match = self.handler.match(window)
            if match and self.handler.is_first_line_match():
                count += 1
                if output_format:
                    out.write(output_format.format(count, match))
                else:
                    out.write(match + "\n")
