# Ветвление в Python


# 1 Фишки ветвления

# 1.1 Проверка числа на чётность

number = 0

if number % 2 == 0:
	print( f"Число {number} чётное" )
else:
	print( f"Число {number} нечётное" )

# 1.2 Сравнение двух чисел

number1 = 10
number2 = 20

if number1 > number2:
	print( f"Число {number1} больше числа {number2}" )
elif number1 < number2:
	print( f"Число {number1} меньше числа {number2}" )
else:
	print( f"Числа {number1} и {number2} одинаковы" )

# 1.3 Проверка строки на длину

length = 10
string = "abcdef"

if len( string ) > length:
	print( f"Строка {string} длиннее {length} символов" )
elif len( string ) < length:
	print( f"Строка {string} короче {length} символов" )
else:
	print( f"Строка {string} равна {length} символам" )
