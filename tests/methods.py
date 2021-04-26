# Операторы


# 1 Основные строковые методы

# 1.1 capitalize()

"this is string".capitalize()  # 'This is string'
"THIS IS STRING".capitalize()  # 'This is string'
"ThIs IS STRing".capitalize()  # 'This is string'

# 1.2 title()

"this is string".title()  # 'This Is String'
"THIS IS STRING".title()  # 'This Is String'
"ThIs IS STRing".title()  # 'This Is String'

# 1.3 upper()

"big string".upper()  # 'BIG STRING'
"BIG STRING".upper()  # 'BIG STRING'
"BiG STRing".upper()  # 'BIG STRING'

# 1.4 lower()

"just string".capitalize()  # 'just string'
"JUST STRING".capitalize()  # 'just string'
"JuSt STRing".capitalize()  # 'just string'

# 1.5 count()

s = "ab Cb ab Cb ab cb ab"

s.count("b")   # 7
s.count("ab")  # 4
s.count("cb")  # 1
s.count("Cb")  # 2
s.count("A")   # 0

# 1.6 find()

s = "ab Cb ab Cb ab cb ab"

s.find("a")   # 0
s.find("b")   # 1
s.find("ab")  # 0
s.find("Cb")  # 3
s.find("cb")  # 15
s.find("A")   # -1

# 1.7 strip()

"  some data  ".strip()      # 'some data'
" some data   ".strip(" ")   # 'some data'
"_= data -=".strip("_=- ")   # 'data'
"bac[data]bca".strip("abc")  # '[data]'

# 1.8 replace()

"Apple is green".replace( "green", "red" )     # 'Apple is red'
"Apple is green".replace( "green", "red", 0 )  # 'Apple is green'

"ha-ha-ha-ha-ha".replace( "ha", "ho" )         # 'ho-ho-ho-ho-ho'
"ha-ha-ha-ha-ha".replace( "ha", "ho", -1 )     # 'ho-ho-ho-ho-ho'
"ha-ha-ha-ha-ha".replace( "ha", "ho", 2 )      # 'ho-ho-ha-ha-ha'
