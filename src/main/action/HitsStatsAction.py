# -*- encoding=utf8 -*-
'''
Created on Apr 9, 2013

@author: eric
'''
from src.main.result.HitsResult import HitsResult
from src.main.scanner.LineScanner import LineScanner
import time

class HitsStatsAction(object):
    '''
        点击率统计分析报告
    '''

    def __init__(self, handler, dest_file, *filenames):
        '''
            @param handler: 行处理句柄
            @param dest_file: 输出文件
            @param *filenames: 待处理文件 
        '''
        self.handler = handler
        self.filenames = filenames
        self.dest_file = dest_file
    
    def action(self, top=0, single_report=False, output_format=None):
        if single_report:
            self.__generate_single_report(top, output_format)
        else:
            self.__generate_reports(top, output_format)
            
    def __get_extension(self, filename):
        index = filename.rfind(".")
        extension = filename[index+1:]
        name = filename[:index]
        return (name, extension)
            
    def __generate_reports(self, top, output_format):
        name, extension = self.__get_extension(self.dest_file)
        for index,filename in enumerate(self.filenames):
            scanner = LineScanner(filename)
            hit_result = HitsResult(output_format)
            print "total lines: {0}".format(scanner.lines_count())
            start = time.clock();
            for line in scanner:
                key = self.handler.match(line)
                if key:
                    hit_result.hit(key)
            hit_result.output("{0}_{1}.{2}".format(name, index, extension), top)
            end = time.clock();
            print "it takes {0} seconds".format(end - start)
        
    def __generate_single_report(self, top, output_format):
        hits_result = HitsResult(output_format)
        scanner = LineScanner(*self.filenames)
        print "total lines: {0}".format(scanner.lines_count())
        start = time.clock();
        for line in scanner:
            key = self.handler.match(line)
            if key :
                hits_result.hit(key);
        
        hits_result.output(self.dest_file, top)
        end = time.clock();
        print "it takes {0} seconds".format(end - start)
            
            