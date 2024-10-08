

class Person:
	def __init__(self, name: str, age: int):
		self.name: str = name
		self.age: int = age

	def display_info(self):
		print(f'Имя {self.name}')
		print(f'Возраст {self.age}')


class Student(Person):
	def __init__(self, name: str, age: int, university: str, average_grade):
		super().__init__(name, age)
		self.university = university
		self.average_grade = average_grade

	def display_info(self):
		super().display_info()
		print(f'Учебнле заведение {self.university}')
		print(f'Средний бал {self.average_grade}')


student = Student()
student.display_info()


