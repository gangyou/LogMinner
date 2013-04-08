# -*- coding=utf8 -*-
import copy, os
from UserDict import UserDict

"""
	挖掘结果集，提供计数
"""
class MinningResult(UserDict):
	def __init__(self):
		UserDict.__init__(self)

	'''
		增加结果集计数
		@param key: 
		@return: 更新后的计数
	'''
	def hit(self, key):
		if not key: return
		if key in self:
			self[key] += 1
		else:
			self[key] = 1
		
		return UserDict.get(self, key, 1)
	
	'''
		增加N次计数
		@param key: 需要增加计数的结果集
	'''
	def incr(self, key, step=1):
		for i in range(step):
			self.hit(key)
		return self
	
	"""
		返回结果集完整副本
	"""
	def all(self):
		return copy.copy(self.storage)

	"""
		获得结果集的一个计数
	"""
	def get(self, key): 
		return UserDict.get(self, key, 0)

	"""
		获得当前结果集大小
	"""
	def size(self): return len(self)
	def len(self): return len(self)
			
	def __sort(self):
		return sorted(self.items(), cmp=lambda x, y: cmp(y[1], x[1]))

	"""
		结果集中，计数前N项
		@param n: 项数量
	"""
	def top(self, n):
		if n > len(self):
			n = len(self)
		sorted_list = self.__sort()
		return sorted_list[0:n]

	def __get_old_name(self, filename):
		index = filename.rfind("/")
		if index > 0:
			index += 1
			return filename[index:]
		else:
			return filename

	def __create_result_dir(self, filename):
		directory = "result"
		prefix = "result_"
		if not os.path.exists(directory):
			os.mkdir(directory)
		return os.path.join(directory, prefix + filename)

	'''
		以文本形式输出结果集
		@param filename: 保存结果集的文本文件名称
		@param top: 输出结果集中的前 top 项，0代表全部输出
	'''
	def output(self, filename="minning_result.txt", top=0):
		filename = self.__get_old_name(filename)
		new_filename = self.__create_result_dir(filename)
		if top:
			with open(new_filename, 'w') as out:
				for item in self.top(top):
					out.write(str(item) + "\n")
		else:
			result = self.__sort()
			with open(new_filename, 'w') as out:
				for item in result:
					out.write(str(item) + "\n")

	'''
		合并结果集, 不改变原有集合
		@param MinningResult: 多个结果集合并 
	'''
	def merge(self, *results):
		for r in results:
			for item in r.items():
				key = item[0]
				value = item[1]
				self.incr(key, value)
		return self

	'''
		清空结果集
	'''
	def close(self):
		self.storage = {}
