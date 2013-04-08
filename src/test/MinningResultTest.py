# -*- coding=utf8 -*-
import unittest
from src.main.result.MinningResult import MinningResult
class MinningResultTest(unittest.TestCase):

	def setUp(self):
		self.result = MinningResult()

	def tearDown(self):
		self.result.close()

	def test_get(self):
		bar_is_never_hit = self.result.get("bar")
		self.assertEqual(0, bar_is_never_hit)

		self.result.hit("bar")
		self.assertEqual(1, self.result.get("bar"))

		self.result.hit("bar")
		self.assertEqual(2, self.result.get("bar"))

	def test_size(self):
		for i in range(10):
			self.result.hit(str(i))

		self.assertEqual(10, self.result.size())

	def test_hit(self):
		self.result.hit("foo")
		times = self.result.hit("foo")
		bar_times = self.result.hit("bar")
		self.assertEqual(2, times)
		self.assertEqual(1, bar_times)


	def __build_test_data(self):
		for i in range(10):
			self.result.hit("most")
		for i in range(5):
			self.result.hit("medium")
		self.result.hit("lest")
		
	def test_top(self):
		self.__build_test_data()

		result = self.result.top(1)
		self.assertEqual("most", result[0][0])
		self.assertEqual(10, result[0][1])

		result = self.result.top(2)
		self.assertEqual("most", result[0][0])
		self.assertEqual(10, result[0][1])
		self.assertEqual("medium", result[1][0])
		self.assertEqual(5, result[1][1])

	def test_output(self):
		self.__build_test_data()
		self.result.output()
		self.result.output('../target/output.txt')
		self.result.output('../target/output_sorted.txt', True)

	def test_merge(self):
		result1 = MinningResult()
		result2 = MinningResult()
		for i in range(5):
			result1.hit("foo")
			result1.hit("bar")
		for i in range(10):
			result2.hit("foo")

		result = result1.merge(result2)

		foo_hit_times = result.get("foo")
		bar_hit_times = result.get("bar")

		self.assertEqual(15, foo_hit_times)
		self.assertEqual(5, bar_hit_times)

if __name__ == '__main__':
	unittest.main()		
