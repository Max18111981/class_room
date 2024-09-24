

# class Human:
# 	def __init__(self, name: str, age: int):
# 		self._name: str = Human._validate_name(name)
# 		self._age: int = Human._validate_age(age)
#
# 	@staticmethod
# 	def _validate_name(name: str):
# 		if name.isalpha():
# 			return name
# 		raise Exception('Имя должнло содержать только буквы')
#
# 	@staticmethod
# 	def _validate_age(age: int):
# 		if 0 < age <= 180:
# 			return age
# 		raise Exception('Возраст должене быть от 1 до 100')
#
# 	def __str__(self):
# 		return f'{self._name} ({self._age})'
#
#
# class Builder(Human):
# 	def __init__(self, name: str, age: int, work_type):
# 		super().__init__(name, age)
# 		self.__work_type: str = work_type
#
#
# class Pilot(Human):
# 	def __init__(self, name: str, age: int, health: int):
# 		super().__init__(name, age)
# 		self.__health: int = health
#
# 	def is_health(self):
# 		if self.__health < 10:
# 			return False
# 		return None
#
#
# class Sailor(Human):
# 	pass


class Passport:
	def __init__(self, name: str, surname: str, date_of_birth: str, number_passport: int):
		self.__name: str = Passport._validate_name(name)
		self.__surname: str = Passport._validate_surname(surname)
		self.__date_of_birth: str = date_of_birth
		self.__number_passport: int = Passport._validate_number_passport(number_passport)

	@staticmethod
	def _validate_name(name: str):
		if name.isalpha():
			return name
		raise Exception('Имя должнло содержать только буквы')

	@staticmethod
	def _validate_surname(surname: str):
		if surname.isalpha():
			return surname
		raise Exception('Фамилия должнло содержать только буквы')

	@staticmethod
	def _validate_number_passport(number_passport: int):
		if len(str(number_passport)) == 6:
			return number_passport
		raise Exception('Номер паспорта должен быть равет шести цифрам')

