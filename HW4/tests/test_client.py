
import unittest
from socket import socket, AF_INET, SOCK_STREAM
from unittest.mock import Mock

from HW4 import Client


class Client_Tests(unittest.TestCase):

    def setUp(self):
        self.server_addr = 'localhost'
        self.server_port = 7777
        self.socket = socket(AF_INET, SOCK_STREAM)


    def test_presence_mock(self):
        mock_socket = Mock(return_value='')
        mock_send = Mock()
        mock_recv = Mock(return_value={'response': '200', 'time': 1612953360})
        Client.socket.recv = mock_socket
        Client.send_message = mock_send
        Client.get_data_from_message = mock_recv
        self.socket.connect((self.server_addr, self.server_port ))  # .connect -  Устанавливаем соедение с сервером
        self.assertEqual(Client.presence(self.socket), {'response': '200', 'time': 1612953360})

    def tearDown(self):
        self.socket.close()


if __name__ == '__main__':
    unittest.main()