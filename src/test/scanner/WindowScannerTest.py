# -*- coding=utf8 -*-
'''
Created on Apr 8, 2013

@author: eric
'''

import unittest, os
from src.main.scanner.WindowScanner import WindowScanner

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_read(self):
        size = 10
        filepath = "../resources/window_scanner_test.txt"
        # 创建10行的窗口大小
        scanner = WindowScanner(filepath, size)
        
        last_win = None
        for win in scanner:
            self.assertEqual(size, len(win.split(os.linesep)) - 1)
            last_win = win
            
        last_win_lines = last_win.split(os.linesep)
        
        lines = []
        with open(filepath) as f:
            for line in f:
                lines.append(line)
        last_ten_lines = lines[-size:]
        last_ten_lines = map(lambda x: x.replace(os.linesep, ""), last_ten_lines)
        self.assertEqual(last_win_lines[:-1], last_ten_lines)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
