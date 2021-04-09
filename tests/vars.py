# Типы переменных


# 1 Числовые типы

# 1.1 Целочисленные

digit = 1
sum = 1000
temp = -43

# 1.2 Вещественные

pi = 3.14
price = 449.99
population = 8e9

# 1.3 Комплексные

z = 3 + 7j
float_complex = 1.2 + 10.5j
minus_complex = -2 + -2.5j


# 2 Строковые

hash = "7ihg89wqp8yghwty4t8p9g8ibqup98gbF8903P8IG8Ffe3jceP9rtg78ufr3"
char = "a"
text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
json = "{ 'orderID': 12345 }"
num  = "12345"


# 3 Логические

is_apple_red = True
evil_is_good = False
boolean = True


# 2 Преобразования

# 2.1 Неявные преобразования

int1 = 2
int2 = 4
float1 = 0.5

x = int1 + float1
y = int1 / int2

# 2.2 Явные преобразования

# 2.2.1 int

to_int1 = int(2.0)  # 2
to_int2 = int('2')  # 2

# 2.2.2 float

to_float1 = float(2)      # 2.0
to_float2 = float('2')    # 2.0
to_float3 = float('2.0')  # 2.0

# 2.2.3 complex

to_complex1 = complex(2)             # (2+0j)
to_complex2 = complex(2, 4)          # (2+4j)
to_complex3 = complex(2.5)           # (2.5+0j)
to_complex4 = complex(2.5, 2)        # (2.5+2j)
to_complex5 = complex('2')           # (2+0j)
to_complex6 = complex('2', '4')      # (2+4j)
to_complex7 = complex('2.5')         # (2.5+0j)
to_complex8 = complex('2.5', '3.1')  # (2.5+3.1j)

# 2.2.4 str

to_str1 = str(2)          # '2'
to_str2 = str(2.0)        # '2.0'
to_str3 = str(2+2j)       # '(2+2j)'
to_str4 = str([1, 2, 3])  # '[1, 2, 3]'
to_str5 = str(True)       # 'True'
to_str6 = str('abc')      # 'abc'

# 2.2.5 bool

to_bool   = bool()           # False
to_bool1  = bool(1)          # True
to_bool2  = bool(0)          # False
to_bool3  = bool(1.0)        # True
to_bool4  = bool(0.0)        # False
to_bool5  = bool(1+1j)       # True
to_bool6  = bool(0+0j)       # False
to_bool7  = bool([1, 2, 3])  # True
to_bool8  = bool([])         # False
to_bool9  = bool(True)       # True
to_bool10 = bool(False)      # False
to_bool11 = bool('abc')      # True
to_bool12 = bool('')         # False
