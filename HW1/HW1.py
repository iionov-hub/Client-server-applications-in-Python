# 1 Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление
# в формат Unicode и также проверить тип и содержимое переменных.


v_text = 'разработка'
print(v_text)
print(type(v_text))


v_text = 'сокет'
print(v_text)
print(type(v_text))


v_text = 'декоратор'
print(v_text)
print(type(v_text))

print('--------------------------------')


v_text = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
print(v_text)
print(type(v_text))

v_text = '\u0441\u043e\u043a\u0435\u0442'
print(v_text)
print(type(v_text))

v_text = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(v_text)
print(type(v_text))



# 2. Каждое из слов «class», «function», «method» записать
# в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

v_text = 'class'
v_text = bytes(v_text, encoding = 'utf-8')
print(v_text, type(v_text), len(v_text))

v_text = 'function'
v_text = bytes(v_text, encoding = 'utf-8')
print(v_text, type(v_text), len(v_text))

v_text = 'method'
v_text = bytes(v_text, encoding = 'utf-8')
print(v_text, type(v_text), len(v_text))

