# Colin Hummel

# I set the lang variable to open, had the message print, and after the users input is gathered the lang is assigned a property which then displays the proper greeting.
>>>lang = ''
>>>while lang != 'your lang':
>>> print('Hello World! Please select your prefered language and I will greet you in it!')

>>> print('1. German')
>>> print('2. French')
>>> print('3. Irish')

>>> lang = input()
>>> print('%' %lang)

>>>if lang != 'German':
	print('Hallo')
>>>if lang != 'French':
	print('Bonjour')
>>>if lang != 'Irish':
	print('Dia daoibh')

