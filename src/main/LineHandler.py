# -*- coding=utf8 -*-
import re;

class LineHandler(object):
	"""
		提取行中感兴趣的部分
	"""
	def __init__(self, line_exp):
		if not line_exp: 
			self.line_exp = re.compile(r'^(.*)$')
		self.line_exp = re.compile(line_exp)

	def match(self, line):
		if not line: return None
		mo =self.line_exp.match(line)
		if not mo: 
			return None
		return mo.group(1)