# Операторы


# 1 Математические

# 1.1 Присваивание

integer = 2
string = "foo"
arr = [ 1, 2, 3 ]
four = 2 + 2

# 1.2 Сложение

sum_int = 20 + 25 + 25   # 70
sum_str = "ab" + "cd"    # "abcd"
sum_arr = [ 1 ] + [ 2 ]  # [ 1, 2 ]

# 1.3 Вычитание

sub1 = 20 - 10  # 10
sub2 = 20 - 20  # 0
sub3 = 20 - 30  # -10

# 1.4 Умножение

mult_int = 20 * 20 * 20  # 8000
mult_str = "haha" * 3    # "hahahahahaha"
mult_arr = [ 1, 2 ] * 4  # [ 1, 2, 1, 2, 1, 2, 1, 2 ]

# 1.5 Деление

div1 = 20 / 10  # 2
div2 = 15 / 2   # 7.5
div3 = 2 / 3    # 0.6666666666666666

# 1.6 Возведение в степень

pow1 = 0 ** 1000  # 0
pow2 = 1000 ** 0  # 1
pow3 = 2 ** 20    # 1048576

# 1.7 Целочисленное деление

int_div1 = 100 // 2   # 50
int_div2 = 80 // 3    # 26
int_div3 = 150 // 20  # 7

# 1.8 Остаток от деления

mod1 = 100 % 2   # 0
mod2 = 80 % 3    # 2
mod3 = 150 % 20  # 10


# 2 Логические

# 2.1 Сравнение

eq1 = 1234 == 1234    # True
eq2 = 1234 == 1235    # False
eq3 = "ab" == "ab"    # True
eq4 = [ 1 ] == [ 1 ]  # True

# 2.2 Больше

big1 = 1000 > 900     # True
big2 = 900 > 1000     # False
big3 = "abc" > "ab"   # True
big4 = [ 2 ] > [ 1 ]  # True

# 2.3 Меньше

min1 = 9990 < 10000   # True
min2 = 6500 < 4500    # False
min3 = "xy" < "xyz"   # True
min4 = [ 3 ] < [ 5 ]  # True

# 2.4 Больше или равно

big_eq1 = 90 >= 80  # True
big_eq2 = 80 >= 80  # True
big_eq3 = 70 >= 80  # False

# 2.5 Меньше или равно

min_eq1 = 400 <= 500  # True
min_eq2 = 400 <= 400  # True
min_eq3 = 400 <= 300  # False


# 3 Операторы взаимодействия с пользователем

# 3.1 Вывод в консоль

print()                     #
print( 20 )                 # 20
print( 'Hello world!' )     # Hello world!
print( 20 + 20 - 20 )       # 20
print( '20 + 20 - 20' )     # 20 + 20 - 20
print( [ 1, [ 2 ], '3' ] )  # [ 1, [ 2 ], '3' ]

var = 'It`s a variable'
print( var )                # 'It`s a variable'

# 3.2 Получение ввода пользователя

input()
save = input()
input('Введите число: ')
