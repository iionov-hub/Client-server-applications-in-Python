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

# 3 Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

v_texts = ['attribute', 'класс', 'функция', 'type']
v_texts_i = []
for v_text in v_texts:
    byte = v_text.encode()
    print(v_text,byte)
    if '\\' in str(byte):
        v_texts_i.append(v_text)
# print(f'Невозможно записать в байтовом типе слова: {", ".join(v_texts_i)}')
print(f'Невозможно записать в байтовом типе слова: {v_texts_i}')



# 4 Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование
# (используя методы encode и decode).

for v_text in ['разработка', 'администрирование', 'protocol', 'standard']:
    a = v_text.encode('utf-8')
    b = a.decode('utf-8', 'replace')
    print(a, b, v_text)


# 5 Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
# из байтовового в строковый тип на кириллице.

import subprocess

for ping in ['yandex.ru', 'youtube.com']:
    v_text = ['ping', ping]
    ya_you_ping = subprocess.Popen(v_text, stdout=subprocess.PIPE)
    for line in ya_you_ping.stdout:
        print(line.decode('CP1125').encode('utf-8').decode('utf-8'))


# 6 Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое

v_text = open('test_file.txt', 'w', encoding='utf-8')
v_text.write('сетевое программирование сокет декоратор')
v_text.close()
print(type(v_text))

with open('test_file.txt', encoding='utf-8') as v_text:
    for v_texts in v_text:
        print(v_texts, end="")