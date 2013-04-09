# -*- coding=utf8 -*-
import re;

'''
	返回符合符合正则表达式的行
'''

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
			self.line_exp = re.compile(r'^(.*)$', flags)
		self.line_exp = re.compile(line_exp, flags)
		
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
		mo = self.line_exp.match(lines)
		match_part = self.__get_match_part(mo)
		return match_part
