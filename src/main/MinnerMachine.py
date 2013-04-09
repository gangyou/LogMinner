# -*- coding=utf8 -*-
from src.main.result.HitsResult import HitsResult
class MinnerMachine(object):
	def __init__(self, line_handler, *filenames):
		self.line_handler = line_handler
		if len(filenames) >= 1: 
			self.filenames = list(filenames)

	def action(self, top=0, single_report=False):
		if single_report:
			for filename in self.filenames:
				self.__process_single_file(filename, top)
		else:
			self.__process_batch_file(self.filenames, top)

	def __process_single_file(self, filename, top):
		print "Processing " + filename
		result = HitsResult()
		with open(filename) as f:
			for line in f:
				match = self.line_handler.match(line)
				if match: result.hit(match)
		result.output("result_" + filename, top)

	def __process_batch_file(self, filenames, top):
		result = HitsResult()
		for filename in filenames:
			print "Processing " + filename
			with open(filename) as f:
				for line in f:
					match = self.line_handler.match(line)
					if match: result.hit(match)
		result.output("total.log", top)

	
