from socket import *
import time
import json

def get_data_from_message(response):
    response_str = response.decode('utf-8') # идёт расшифровка сообщения переданная от клиента, переданная от server
    return json.loads(response_str)

def send_message(s, msg_response): # принимаем параметры отправленные от клиента
    msg = json.dumps(msg_response)
    s.send(bytes(msg, encoding="utf-8")) # отправялем сообщение


def presence(s):
    msg_presence = { # Формируем presence-сообщение
        "action": "presence",
        "time": int(time.time()),
        "type": "status",
        "user": {
            "account_name": "Igor",
            "status": "connect"
        }
    }

    send_message(s, msg_presence) # переходим в фукнцию и отправляем сообщение с параметрами

    data = get_data_from_message(s.recv(1000000))
    print('Сообщение от сервера: ', data)


def main():
    s = socket(AF_INET, SOCK_STREAM) # sockect - Создаём сокет TCP
    s.connect(('localhost', 7777)) # .connect -  Устанавливаем соедение с сервером

    presence(s) # переходим в функцию для отправки presence-сообщениz

    s.close() # .close - Закрыть соединение

if __name__ == '__main__':
    main()