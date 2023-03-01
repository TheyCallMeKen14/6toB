a = 20
b = 30
c = 10
d = 50
booleano = True
flotante = 3.45
spring = "Hola"
listas = 20, 30, 10, 50 
diccionario = "Nombre" ; "Jose" , "edad" : 15, "is,dead" : False 

resultado = a + b
print(resultado)

# Operaciones básicas:

 123 + 222
#  345

  1.5 * 4
# 6.0

2 ** 100
# 1267650600228229401496703205376

  len(893)
# TypeError: object of type 'int' has no len()
  len("893")
# 3
 
 len([2, 3, 4, 5])
# 4
 
 len(str(2 ** 1000000))
#  ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

random.choice([1, 2, 3, 4])
#  NameError: name 'random' is not defined
  
  st + "Hola"
#  NameError: name 'st' is not defined
  
  import math
#
  
  Math.pi
# NameError: name 'Math' is not defined

  math.sqrt(85)
# 9.219544457292887

  import random
#

  random.random()
# 0.5679999444334052

  st = 'Spam'
#  spam

  len(st)
#  4
 
  st[0]
# 'S'

  st[-1]
#  'm'

  st[1:3]
# 'pa'

  st[1:]
# 'pam'

  st[:]
#  'Spam'

  st * 5
# 'SpamSpamSpamSpamSpam'

  st[0] = 'z'
# TypeError: 'str' object does not support item assignment

  st = 'z' + st[1:]
#

  print(st)
# zpam


# Transformar string a lista:

  S = 'shrubbery'
#

  L = list(S)
#

  L
# ['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']

  L[1] = 'c'
# 
 
  B = bytearray(b'spam')
#
 
  B.extend(b'eggs')
#
 
  B
# bytearray(b'spameggs')

  B.decode()
# 'spameggs'
 
# Métodos especiales para strings:
 
  S = 'Spam'
#

  S.find('pa')
# 1
 
  S
# 'Spam'
 
  S.replace('pa', 'XYZ')
# 'SXYZm'

  S
# 'Spam' 
 
  line = 'aaa,bbb,ccccc,dd'
#
 
 line.split(',')
# ['aaa', 'bbb', 'ccccc', 'dd'] 
 
 S = 'spam'
#
 
 S.upper()
#
 
 S.isalpha()
# True
 
  line = 'aaa,bbb,ccccc,dd\n'
#  
 
  line.rstrip()
# 'aaa,bbb,ccccc,dd'

  line.rstrip().split(',')
# ['aaa', 'bbb', 'ccccc', 'dd']

#Plantillas para strings:

  '%s, eggs, and %s' % ('spam', 'SPAM!')
# 'spam, eggs, and SPAM!'

  '{0}, eggs, and {1}'.format('spam', 'SPAM!')
# 'spam, eggs, and SPAM!'

  '{}, eggs, and {}'.format('spam', 'SPAM!')
# 'spam, eggs, and SPAM!'

   f'{S}, eggs, and {line}'
#  'spam, eggs, and aaa,bbb,ccccc,dd\n'

# Visualizar los métodos de un objecto:

   dir(S) # S es un string
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

   help(S.replace)
# Help on built-in function replace: replace(old, new, count=-1, /) method of builtins.str instance Return a copy with all occurrences of substring old replaced by new.countMaximum number of occurrences to replace.-1 (the default value) means replace all occurrences.If the optional argument count is given, only the first count occurrences are replaced.

   S = 'A\nB\tC'
# 
 
   len(S)
# 5
 
   ord('\n')
# 10

  S = 'A\0B\0C'
# 
 
  len(S)
# 5

  S
# 'A\x00B\x00C'
 
msg = """
aaaaaaaaaaaaa
Strings | 105bbb'''bbbbbbbbbb""bbbbbbb'bbbb
cccccccccccccc
"""
#

  msg
# '\naaaaaaaaaaaaa\nStrings | 105bbb\'\'\'bbbbbbbbbb""bbbbbbb\'bbbb\ncccccccccccccc\n'

# Entradas de usuario:

  color = input("Introduce el color de tu camisa?: ")
# Introduce el color de tu camisa?:

  print(color)
# 

  n = int(input("Cuantas camisas tienes?: "))
# Cuantas camisas tienes?:

  print(n)
# NameError: name 'n' is not defined

  price = float(input("Cuanto costo la mas bonita?: "))
#  Cuanto costo la mas bonita?:  
  
  print(price) 
# NameError: name 'price' is not defined
  
#Python: Expresiones Regulares

  import re

  match = re.match('Hello[ \t]*(.*)world', 'Hello
#SyntaxError: unterminated string literal (detected at line 1)

  match.group(1)
# NameError: name 'match' is not defined

  match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')  
#
 
  match.groups()
#('usr', 'home', 'lumberjack')
 
 re.split('[/:]', '/usr/home/lumberjack')
#['', 'usr', 'home', 'lumberjack']
 
  phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# 
 
  mo = phone_num_regex.search('My number is 415-555-4242.')
#

  print(f'Phone number found: {mo.group()}')
#Phone number found: 415-555-4242
 
 
  phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# 
 
  mo = phone_num_regex.search('My number is 415-555-4242.') 
#

  mo.group(1)
#'415'
  mo.group(2)
#'555-4242'
  
  mo.group(0)  
#'415-555-4242' 
  
  mo.group() 
#'415-555-4242'
 
  hero_regex = re.compile (r'Batman|Tina Fey')
# 
 
  mo1 = hero_regex.search('Batman and Tina Fey.') 
#

  mo1 = hero_regex.search('Batman and Tina Fey.')
#

  mo1.group()
#'Batman' 
 
   mo2 = hero_regex.search('Tina Fey and Batman.')
#

  mo2.group()
#'Tina Fey' 
 
 
 
 
  
 
 
 