# -*- coding=utf8 -*-
'''
Created on Apr 9, 2013

@author: eric
'''
import unittest
from src.main.handler.RegexpHandler import RegexpHandler
from src.main.action.HitsStatsAction import HitsStatsAction
import os


class HitsStatsActionTest(unittest.TestCase):
   

    def test_normal_single_report(self):
        #正则匹配行
        handler = RegexpHandler("labore")
        dest_file = "../resources/report.txt"
        #点击率统计
        action = HitsStatsAction(handler, dest_file, '../resources/hits_stats_test.txt')
        #生成文件放在同一个报告中
        action.action(single_report=True)
        
        f = open(dest_file)
        result = f.readline();
        self.assertEqual(result, "('labore', 32)\n")
        
        action = HitsStatsAction(handler, dest_file, '../resources/hits_stats_test.txt', 
                                 '../resources/hits_stats_test.txt')
        action.action(single_report=True)
        f = open(dest_file)
        result = f.readline()
        self.assertEqual(result, "('labore', 64)\n")
        
    def test_format_single_report(self):
        handler = RegexpHandler("labore")
        dest_file = "../resources/report.txt"
        
        action = HitsStatsAction(handler, dest_file, '../resources/hits_stats_test.txt')
        action.action(single_report=True, output_format="key: {0}, value: {1}")
        
        f = open(dest_file)
        result = f.readline();
        self.assertEqual(result, "key: labore, value: 32\n")
        
    def test_normal_multi_reports(self):
        handler = RegexpHandler("labore")
        dest_file = "../resources/report.txt"
        dest_file_excepts = ['../resources/report_0.txt', '../resources/report_1.txt']
        
        action = HitsStatsAction(handler, dest_file, '../resources/hits_stats_test.txt', 
                                 '../resources/hits_stats_test.txt')
        action.action()
        
        for f in dest_file_excepts:
            self.assertTrue(os.path.exists(f), str(f) + " is not exists")
            
        lines_in_file1 = open(dest_file_excepts[0]).readlines()
        lines_in_file2 = open(dest_file_excepts[1]).readlines()
        for line1, line2 in zip(lines_in_file1, lines_in_file2):
            self.assertEqual(line1, line2)
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
