# -*- coding=utf8 -*-
import re;

'''
	返回符合符合正则表达式的行
'''
import os

# flags
IGNORECASE = re.IGNORECASE
LOCALE = re.LOCALE
UNICODE = re.UNICODE
MULTILINE = re.MULTILINE
DOTALL = re.DOTALL
VERBOSE = re.VERBOSE

class RegexpHandler(object):
	
	def __init__(self, line_exp=None, flags=0):
		if not line_exp: 
			self.line_exp = r'^(.*)$'
		self.line_exp = line_exp
		self.flags = flags
		
	def __get_match_part(self, mo):
		match_part = ""
		try:
			match_part = mo.group(1)
		except IndexError:
			match_part = mo.group(0)
		finally:
			return match_part

	'''
		根据正则表达式匹配一行中感兴趣内容，返回第一个匹配分组
	'''
	def match(self, lines):
		if not lines: return None
		#记录当前访问行
		self.lines = lines
		self.mo = re.search(self.line_exp, lines, self.flags)
		match_part = self.__get_match_part(self.mo)
		return match_part
	
	def is_first_line_match(self):
		if not hasattr(self, 'mo'): return False
		if not self.mo: return False
		first_line_end = self.lines.find(os.linesep)
		try:
			start = self.mo.start(1)
			if start < first_line_end: return True
			else: return False
		except IndexError:
			start = self.mo.start(0)
			if start < first_line_end: return True
			else: return False
