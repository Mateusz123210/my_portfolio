import copy
import pyaes
from message import Message
from connections import Connections

class TasksExecutor:

    def __init__(self, clients):
        self.clients = clients
        self.connections = Connections()

        pass

    def execute(self, dictionary: dict, data):
        if 'id' in dictionary.keys() and 'receiver_id' in dictionary.keys()\
                and 'method' in dictionary.keys() and 'message' in dictionary.keys():
            if dictionary.get("method") == "key":
                return self.transfer_rsa_key(dictionary)
            elif dictionary.get("method") == "key-response":
                return "5"
        elif 'method' in dictionary.keys():
            method = dictionary.get('method')
            if method == 'hello':
                return self.hello(dictionary)
            elif method == 'get-message':
                return self.return_messages(dictionary)
            elif method == 'get-rsa':
                return self.return_rsa_key(dictionary)
            elif method == 'get-aes':
                return self.return_aes_keys(dictionary)
            elif method == "send-aes":
                return self.send_aes_keys(dictionary, data)
            elif method == "get_aes":
                return self.return_aes_keys(dictionary)
        elif 'id' in dictionary.keys():
            return self.execute_encrypted(dictionary)
        elif 'from' in dictionary.keys():
            return self.cache_message(dictionary)

        return None

    def return_aes_keys(self, dictionary):
        if not ('id' in dictionary.keys()):
            return None
        client_list, client = self.find_client(dictionary.get('id'))
        if client is None:
            self.clients.mutex_unlock()
            return None
        aes_key = client.get_aes_key()
        self.clients.mutex_unlock()
        con = self.connections.get_connections_senders(dictionary.get('id'))
        a = []
        for i in con:
            a.append(i.pop_aes_messages())

        if len(a) > 0:
            string = ""
            for b in a:
                for c in b:
                    string += str(c)
                    string += "{;}"
            string = string[:-3]
            return string

        return ("No available aes keys!")

    def send_aes_keys(self, dictionary, data):
        if not ('id' in dictionary.keys() and 'receiver_id' in dictionary.keys() and 'msg' in dictionary.keys()):
            return None
        client_list, client = self.find_client(dictionary.get('id'))
        if client is None:
            self.clients.mutex_unlock()
            return None
        self.clients.mutex_unlock()
        client_list, client = self.find_client(dictionary.get('receiver_id'))
        if client is None:
            self.clients.mutex_unlock()
            return None
        self.clients.mutex_unlock()
        con = self.connections.get_connection(dictionary.get('id'), dictionary.get('receiver_id'))
        con.add_aes_message(data)
        return "AES added"

    def return_rsa_key(self, dictionary):
        if not ('id' in dictionary.keys()):
            return None
        client_list, client = self.find_client(dictionary.get('id'))
        if client is None:
            self.clients.mutex_unlock()
            return None
        aes_key = client.get_aes_key()
        self.clients.mutex_unlock()
        rsa_keys = self.connections.get_connections(dictionary.get('id'))
        if len(rsa_keys) > 0:
            response = ""
            for a in rsa_keys:
                response += a.to_string()
                response += ';'
            response = response[:-1]
            aes = pyaes.AESModeOfOperationCTR(aes_key)
            response = aes.encrypt(response)
        else:
            aes = pyaes.AESModeOfOperationCTR(aes_key)
            response = aes.encrypt("No available rsa keys!")
        return response

    def transfer_rsa_key(self, dictionary):
        client_list, client = self.find_client(dictionary.get('receiver_id'))
        if client is None:
            self.clients.mutex_unlock()
            return None
        self.clients.mutex_unlock()
        client_list, client = self.find_client(dictionary.get('id'))
        if client is None:
            self.clients.mutex_unlock()
            return None
        aes_key = client.get_aes_key()
        self.clients.mutex_unlock()
        aes = pyaes.AESModeOfOperationCTR(aes_key)
        a = dictionary.get("message").encode("raw_unicode_escape")
        rsa_key = aes.decrypt(a)
        return self.connections.check_and_add_connection(dictionary.get('id'), dictionary.get('receiver_id'), rsa_key)

    def return_messages(self, dictionary):
        if len(dictionary) != 2:
            return None
        if not("id" in dictionary.keys()):
            return None
        client_list, client = self.find_client(dictionary.get('id'))
        if client is None:
            self.clients.mutex_unlock()
            return None
        messages = client.get_messages()
        self.clients.mutex_unlock()
        if len(messages) == 0:
            response = "No messages"
        else:
            response = ""
            for a in messages:
                response += a.to_json_string()
                response += ";;;"
            response = response[:-3]

        return response

    def cache_message(self, dictionary):

        if not('message' in dictionary.keys() and 'to' in dictionary.keys()):
            return None

        client_list, client = self.find_client(dictionary.get('from'))
        if client is None:
            self.clients.mutex_unlock()
            return None
        self.clients.mutex_unlock()
        client_list, client = self.find_client(dictionary.get('to'))
        if client is None:
            self.clients.mutex_unlock()
            return None

        message = Message(dictionary.get("from"), dictionary.get('to'), dictionary.get("message"))
        client.add_message(message)
        aes = pyaes.AESModeOfOperationCTR(client.get_aes_key())
        self.clients.mutex_unlock()
        response = "Message received by server"
        response = aes.encrypt(response)
        return response

    def find_client(self, cl_id):
        clients_list = self.clients.get_clients_list_without_release()
        contains = False
        client = None
        for a in clients_list:
            if a.get_id() == cl_id:
                client = a
                contains = True
                break
        if contains is False:
            return None, None
        return clients_list, client

    def execute_encrypted(self, dictionary):
        request = dictionary
        if not ("message" in request.keys()):
            return None
        cl_id = request.get("id")
        clients_list, client = self.find_client(cl_id)
        cl_ids = []
        cl_nicks = []
        for a in clients_list:
            cl_ids.append(a.get_id())
            cl_nicks.append(a.get_nick())
        cl_ids2 = copy.deepcopy(cl_ids)
        cl_nicks2 = copy.deepcopy(cl_nicks)

        self.clients.mutex_unlock()
        for a in range(len(cl_ids2)):
            if cl_ids2[a] == cl_id:
                del cl_ids2[a]
                del cl_nicks2[a]
                break

        response = ""
        for i in range(len(cl_ids2)):
            response += cl_ids2[i] + ','
            response += cl_nicks2[i] + ','
        if len(response) > 0:
            response = response[:-1]
        if len(response) > 1:
            aes = pyaes.AESModeOfOperationCTR(client.get_aes_key())
            response = aes.encrypt(response)

        return response

    def hello(self, dictionary: dict):
        if len(dictionary) != 2:
            return None
        if not ('message' in dictionary.keys()):
            return None
        message = dictionary.get('message')
        if type(message) != dict:
            return None
        if len(message) != 2:
            return None
        if not ('rsa_key' in message.keys()):
            return None
        rsa_key = message.get('rsa_key')
        if type(rsa_key) != str:
            return None
        if len(rsa_key) != 426:
            return None
        nick = message.get('nick')
        if type(nick) != str:
            return None
        if len(nick) < 5 or len(nick) > 30:
            return None
        if "," in nick:
            return None
        return self.clients.add_to_clients_list(nick, rsa_key)
