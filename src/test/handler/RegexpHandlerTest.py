# -*- coding=utf8 -*-
'''
Created on Apr 8, 2013

@author: eric
'''
import unittest, re
import src.main.handler.RegexpHandler as rh

class RegexpHandlerTest(unittest.TestCase):
    
    def test_specified_match(self):
        line = "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"
        handler = rh.RegexpHandler("labore")
        match = handler.match(line)
        self.assertEqual("labore", match)


    def test_match(self):
        lines_array = ["Hello World\n", "Hello Python\n", "Hello Eric"]
        lines = "".join(lines_array)
        
        handler = rh.RegexpHandler(r"^Hello")
        match = handler.match(lines)
        self.assertEqual("Hello", match)
        
        handler = rh.RegexpHandler(r"^(Hello World)")
        match= handler.match(lines)
        self.assertEqual("Hello World", match)
        
        handler = rh.RegexpHandler(r"World.*?Hello", rh.DOTALL)
        match= handler.match(lines)
        self.assert_("World\nHello", match)


if __name__ == "__main__":
    unittest.main()