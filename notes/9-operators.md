# Операторы


Всё программирование — это преобразование данных. С данными уже ясно, остались преобразования. И эта тема куда обширнее. Первое, что в этом поможет — это операторы.

> Оператор — это встроенная в язык функция или оборот языка

На самом деле, в указанном ранее коде уже было использовано как минимум 2 оператора. Однако их куда больше. Для ясности, они разделяются на группы. Начнём с самых простых и до более сложных.


## Функция

Для начала, разберём, что такое функция.

> Функция — это именованная часть кода, которая принимает некоторые аргументы и возвращает некоторое значение

Понятие функции — ключевое во всех языках и изначально пошло из математики, но сильно преобразилось.

Например, функция `print()`, используемая в главе 5. Она принимает аргумент типа `str` ( т.е. строку ) и выводит её на экран.

Например:

```pycon
>>> print("I can print a text!")
I can print a text!
```

И хотя функции куда более сложные, чем кажется, этой базы для понимания достаточно.


## Математические операторы

Это самый простой и понятный вид операторов, знакомый всем ещё со школы. Да, для читаемости они выглядят просто как символы, но это операторы.

### 1. Присваивание ( `=` )

Данный оператор присваивает части слева значение, вычисленное справа. Он повсеместно использовался в предыдущей главе. Фактически, запись `a = 5` означает "присвой переменной `a` значение `5`".

```python
integer = 2
string = "foo"
arr = [ 1, 2, 3 ]
four = 2 + 2
```

### 2. Сложение ( `+` )

Оператор, производящий собственно сложение двух переменных. Но способен складывать не только числа. К примеру, можно сложить две строки или списка, Python это позволяет. Но складывать разные типы уже нельзя. Это позволяет избежать путаницы.

```python
sum_int = 20 + 25 + 25  # 70
sum_str = "ab" + "cd"   # "abcd"
sum_arr = [ 1 ] + [ 2 ] # [ 1, 2 ]
```

### 3. Вычитание ( `-` )

Оператор, вычитающий правое число из левого. Тут всё просто, так как вычитать можно лишь числа.

```python
sub1 = 20 - 10 # 10
sub2 = 20 - 20 # 0
sub3 = 20 - 30 # -10
```

### 4. Умножение ( `*` )

Оператор, перемножающий два числа. Однако у него есть и ещё одна фишка — перемножение строки или списка на число. Да, этого нигде больше нет, но так можно.

```python
mult_int = 20 * 20 * 20 # 8000
mult_str = "haha" * 3   # "hahahahahaha"
mult_arr = [ 1, 2 ] * 4 # [ 1, 2, 1, 2, 1, 2, 1, 2 ] 
```

### 5. Деление ( `/` )

Оператор, делящий левое число на правое. Как и в математике, делить можно только числа, главное помнить, что на 0 делить нельзя. Иначе Python напомнит об этом, выдав исключение `ZeroDivisionError`.

```python
div1 = 20 / 10 # 2
div2 = 15 / 2  # 7.5
div3 = 2 / 3   # 0.6666666666666666
```

### 6. Возведение в степень ( `**` )

Оператор, возводящий левое число в степень правого. Возводить в степень можно лишь числа.

```python
pow1 = 0 ** 1000 # 0
pow2 = 1000 ** 0 # 1
pow3 = 2 ** 20   # 1048576
```

### 7. Целочисленное деление ( `//` )

Оператор, возвращающий целую часть от результата деления. Делить можно только числа.

```python
int_div1 = 100 // 2  # 50
int_div2 = 80 // 3   # 26
int_div3 = 150 // 20 # 7
```

### 8. Остаток от деления / деление по модулю ( `%` )

Оператор, возвращающий остаток от результата целочисленного деления. Т.е. сколько осталось от изначального числа, при отнимании делимой нацело части. Делить можно только числа.

```python
mod1 = 100 % 2  # 0
mod2 = 80 % 3   # 2
mod3 = 150 % 20 # 10
```


## Сокращённые математические операторы

Программисты — самые ленивые люди на свете. И поэтому, они придумали укоротить некоторые операторы, чтобы не писать одно и тоже. Это применимо лишь к переменным, изменение которых идёт напрямую, но это частый случай.  Как это работает:

```python
# Переменная
var = 100

# Полный оператор сложения
var = var + 100

# Сокращённый оператор сложения
var += 100
```

Можно сказать, что симбиоз сложения и присваивания. И таких операторов несколько.


## Логические операторы

Это операторы сравнения, которые возвращают `True` или `False`. Очень часто такие операторы используются в операторах ветвления.

### 1. Сравнение ( `==` )

Оператор, который возвращает True, если два объекта равны и False в любом другом случае. Не путать его с оператором присваивания ( `=` ).

```python
eq1 = 1234 == 1234   # True
eq2 = 1234 == 1235   # False
eq3 = "ab" == "ab"   # True
eq4 = [ 1 ] == [ 1 ] # True
```

### 2. Больше ( `>` )

Оператор, который возвращает True, если левый объект больше правого и False в любом другом случае.

```python
big1 = 1000 > 900    # True
big2 = 900 > 1000    # False
big3 = "abc" > "ab"  # True
big4 = [ 2 ] > [ 1 ] # True
```

### 3. Меньше ( `<` )

Оператор, который возвращает True, если левый объект меньше правого и False в любом другом случае.

```python
min1 = 9990 < 10000  # True
min2 = 6500 < 4500   # False
min3 = "xy" < "xyz"  # True
min4 = [ 3 ] < [ 5 ] # True
```

### 4. Больше или равно ( `>=` )

Оператор, который возвращает True, если левый объект больше или равен правому и False в любом другом случае.

```python
big_eq1 = 90 >= 80 # True
big_eq2 = 80 >= 80 # True
big_eq3 = 70 >= 80 # False
```

### 5. Меньше или равно ( `<=` )

Оператор, который возвращает True, если левый объект меньше или равен правому и False в любом другом случае.

```python
min_eq1 = 400 <= 500 # True
min_eq2 = 400 <= 400 # True
min_eq3 = 400 <= 300 # False
```


## Операторы взаимодействия с пользователем

Это простые текстовые функции, которые могут использоваться в простых программах.

### 1. Вывод в консоль ( `print()` )

Очень простая функция, главная задача который вывод текста в консоль. Она уже использовалась ранее. Принимает любой объект, который можно напечатать.

```python
print()                    #  
print( 20 )                # 20
print( 'Hello world!' )    # Hello world!
print( 20 + 20 - 20 )      # 20
print( '20 + 20 - 20' )    # 20 + 20 - 20
print( [ 1, [ 2 ], '3' ] ) # [ 1, [ 2 ], '3' ]

var = 'It`s a variable'
print( var )               # 'It`s a variable'
```


### 2. Получение ввода пользователя ( `input()` )

Функция, которая предоставляет пользователю возможность ввода, ждёт его ответа и затем возвращает полученный результат. Важно — эта функция всегда возвращает строку. Так что, даже если пользователь ввёл число, нужно будет сначала явно преобразовать строку в число.

```python
input()
save = input()
input('Введите число: ')
```


### 3. Ничего не делать ( `pass` )

Функция, которая делает... ничего. Это просто заглушка для других операторов. Её применение будет рассмотрено в главе 12.



## Операторы массивов

Массивы ( они же списки, словари, кортежи и множества ), также обладают своими особыми операторами. Они в целом сходно работают для всех типов и очень часто пригождаются при работе с ними:

### 1. Длина массива ( `len()` )

Функция, возвращающая длину объекта Python. На самом деле, она довольно универсальная и применима как ко всем типам массивов, так и к строкам.

```python
len( "abc def abc def" )   # 6
len( [ 1, 2, 3, 4, 5 ] )   # 3
len( ( 1, 2, 3, 4, 5 ) )   # 3
len( { "key": "value" } )  # 1
len( { 1, 2, 3, 4, 5 } )   # 5
```

### 2. Максимум и минимум ( `max()` и `min()` )

Это две функции, которые возвращают максимальное и минимальное значение в массиве соответственно.

> Примечание: в случае словаря, возвращается максимальное / минимальное значение ключа, а не сами значения элементов.

```python
max( [ 1, 2, 3, 4, 5, 6, 7 ] )   # 7
max( ( 1, 2, 3, 4, 5, 6, 7 ) )   # 7
max( { "a" : "b", "c" : "d" } )  # 'c'
max( { 1, 2, 3, 4, 5, 6, 7 } )   # 7

min( [ 1, 2, 3, 4, 5, 6, 7 ] )   # 1
min( ( 1, 2, 3, 4, 5, 6, 7 ) )   # 1
min( { "a" : "b", "c" : "d" } )  # 'a'
min( { 1, 2, 3, 4, 5, 6, 7 } )   # 1
```

### 3. Сумма массива ( `sum()` )

Функция, возвращающая сумму элементов массива.

> Примечание: в случае словаря, складываются лишь числовые ключи

```python
sum( [ 1, 2, 3, 4, 5, 6 ] )  # 21
sum( ( 1, 2, 3, 4, 5, 6 ) )  # 21
sum( { 1: 2, 3: 4, 5: 6 } )  # 9
sum( { 1, 2, 3, 4, 5, 6 } )  # 21
```
