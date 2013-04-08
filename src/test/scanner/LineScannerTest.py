'''
Created on Apr 8, 2013

@author: eric
'''
# -*- coding=utf8 -*-
import unittest
from src.main.scanner.LineScanner import LineScanner

class LineScannerTest(unittest.TestCase):



    def testName(self):
        scanner = LineScanner("../resources/test.txt");
        result = []
        for line in scanner:
            result.append(line)
            
        self.assertEqual(6, len(result))
        self.assertEqual("6", result[len(result) - 1])

if __name__ == "__main__":
    unittest.main()