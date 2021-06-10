from socket import *
import time
import json

def get_data_from_message(response):
    response_str = response.decode('utf-8') # идёт расшифровка сообщения переданная от клиента, переданная от server
    return json.loads(response_str)

def send_message(s, msg_response): # принимаем параметры отправленные от клиента
    msg = json.dumps(msg_response)
    s.send(bytes(msg, encoding="utf-8")) # отправялем сообщение

def send_answer(client):
    msg_response = {
        "response": '200',
        'time': int(time.time())
    }
    send_message(client, msg_response)


def main():

    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    s.bind(('', 7777))                # Присваивает порт 7777
    s.listen(1)                       # Переходит в режим ожидания запросов;


    while True:
        client, addr = s.accept() # принять установку на соединение
        data_client = get_data_from_message(client.recv(1000000)) # Идёт обращение в Json файл, где идёт расшифровка сообщения от клиента
        print('Сообщение: ', data_client, ', было отправлено клиентом: ', addr)

        send_answer(client)

        client.close()

if __name__ == '__main__':
    main()