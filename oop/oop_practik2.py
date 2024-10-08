import math
from abc import abstractmethod


class Shape:
	@abstractmethod
	def get_area(self):
		raise NotImplementedError()


class Rectangle(Shape):
	def __init__(self, length: int, width: int):
		self.length = length
		self.width = width

	def get_area(self):
		return self.length * self.width


class Circle(Shape):
	def __init__(self, radius: float):
		self.radius = radius

	def get_area(self):
		return math.pi * (self.radius ** 2)


