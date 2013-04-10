# -*- coding=utf8 -*-
'''
Created on Apr 9, 2013

@author: eric
'''
import unittest, re
from src.main.handler.RegexpHandler import RegexpHandler
from src.main.action.CustomerPathAction import CustomerPathAction


class CustomerPathActionTest(unittest.TestCase):


    def test_action(self):
        session_id = 'EBCPEAIGCSGLBQJNDMCUHCIOFAIDFJFGAMDJDYGR'
        handler = RegexpHandler(r"^.*?Req Url:(/perbank/.*?\.do).*EMP_SID={0}".format(session_id),re.DOTALL | re.MULTILINE)
        action = CustomerPathAction(handler, "EBCPEAIGCSGLBQJNDMCUHCIOFAIDFJFGAMDJDYGR.txt", "../resources/10w.txt")
        action.action("客户动作: {0} 访问Url: {1}\n")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()