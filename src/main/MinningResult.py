# -*- coding=utf8 -*-
import copy, os

class MinningResult(object):
	def __init__(self):
		self.storage = {}

	def hit(self, key):
		if not key: return
		if key in self.storage:
			self.storage[key] += 1
		else:
			self.storage[key] = 1

	def all(self):
		return copy.copy(self.storage)

	def get(self, key):
		return self.storage.get(key, 0)

	def size(self):
		return len(self.storage)
			
	def __sort(self):
		'''
			sorted by value
		'''
		return sorted(self.storage.items(), cmp=lambda x, y: cmp(y[1], x[1]))

	def top(self, n):
		if n > len(self.storage):
			n = len(self.storage)
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

	def merge(self, *result):
		for r in result:
			dict1, dict2 = self.storage, r.all()
			self.storage = dict((n, dict1.get(n,0) + dict2.get(n, 0)) for n in set(dict1)|set(dict2))
		return self


	def close(self):
		self.storage = {}