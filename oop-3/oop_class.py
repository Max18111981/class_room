class Human:
	def __init__(self, name: str, age: int):
		self._name: str = Human._validate_name(name)
		self._age: int = Human._validate_age(age)

	@staticmethod
	def _validate_name(name: str):
		if name.isalpha():
			return name
		raise Exception('Имя должнло содержать только буквы')

	@staticmethod
	def _validate_age(age: int):
		if 0 < age <= 180:
			return age
		raise Exception('Возраст должене быть от 1 до 100')

	def __str__(self):
		return f'{self._name} ({self._age})'


class Builder(Human):



class Pilot(Human):


class Sailor(Human):