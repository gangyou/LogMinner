# -*- coding=utf8 -*-
import re;

'''
	返回符合符合正则表达式的行
'''
class LineHandler(object):
	
	def __init__(self, line_exp):
		if not line_exp: 
			self.line_exp = re.compile(r'^(.*)$')
		self.line_exp = re.compile(line_exp)

	'''
		根据正则表达式匹配一行中感兴趣内容，返回第一个匹配分组
	'''
	def match(self, line):
		if not line: return None
		mo =self.line_exp.match(line)
		if not mo: 
			return None
		return mo.group(1)