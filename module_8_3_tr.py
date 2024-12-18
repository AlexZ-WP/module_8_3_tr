# class Car:
#     def __init__(self, model, __vin, numbers):
#         self.model = model
#         self._vin = __is_valid_vin(self, vin_number)
#         self.numbers = numbers



class Car:
    def __init__(self, model, __vin , numbers ):
        self.model = model
        self._vin = __vin
        self.numbers = numbers

def __is_valid_vin(self, vin_number):
    vin_number = __vin
    if not isinstance(vin_number, int):
        raise IncorrectVinNumber('Некорректный тип vin номер')
    elif vin_number not in range(1000000, 10000000):
        raise IncorrectVinNumber('Неверный диапазон для vin номера')
    else:
        return Car.vin_number
def __is_valid_numbers(self, numbers):
    if not isinstance(numbers, str):
        raise IncorrectCarNumbers('Некорректный тип данных для номеров')
    elif len(numbers) < 6 < len(numbers):
        raise IncorrectVinNumber('Неверная длина номера')
    else:
        return numbers

class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.massage = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        #super().__init__(numbers)

# class Car(IncorrectVinNumber):
#     def __init__(self, model, __vin, numbers):
#         self.model = model
#         self._vin = __vin
#         self.numbers = numbers
#         super().__is_valid_vin(self, vin_number)
print(dir(Car))
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

print(hasattr(IncorrectVinNumber, '__is_valid_numbers'))
print(hasattr(Car, '__is_valid_numbers'))




