import asyncio
import copy
import os
import time
from multiprocessing.spawn import freeze_support
import websockets
import hashlib
import rsa
import json
import pyaes
from threading import Lock

from PyQt5.QtGui import QColor


class Client:

    def __init__(self):
        self.connection_code = '2432001057066268503415301041693135315399706163881527379982899547'
        self.address = "ws://localhost:7777"

        with open("config.txt","r") as f:
            a = f.read().splitlines()
            self.connection_code = a[0]
            self.address = a[1]

        self.connection_hash = None
        self.public_key = None
        self.private_key = None
        self.response = None
        self.aes = None
        self.id = None
        self.connected = False
        self.connected_persons = []
        self.messages = []
        self.message_lock = Lock()
        self.interface_reference = None

    def set_interface_reference(self, reference):
        self.interface_reference = reference

    def get_id(self):
        return self.id

    def rsa_decrypt(self, string):
        result = []
        for n in range(0, len(string), 256):
            part = string[n:n + 256]
            result.append(rsa.decrypt(part, self.private_key).decode("utf-8"))
        try:
            result = json.loads(''.join(result))
        except ValueError:
            result = None
        return result

    def rsa_decrypt2(self, string, key):
        result = []
        for n in range(0, len(string), 256):
            part = string[n:n + 256]
            result.append(rsa.decrypt(part.encode("raw_unicode_escape"), key).decode("raw_unicode_escape"))
        try:
            result = json.loads(''.join(result))
        except ValueError:
            result = None
        return result

    def rsa_encrypt(self, string, key):
        result = []
        for n in range(0, len(string), 245):
            part = string[n:n + 245]
            result.append(rsa.encrypt(part.encode("utf-8"), key))
        return b''.join(result)

    def rsa_encrypt2(self, string, key):
        result = []
        for n in range(0, len(string), 245):
            part = string[n:n + 245]
            result.append(rsa.encrypt(part.encode("utf-8"), key))
        return b''.join(result)

    async def hello(self, string: str):
        async with websockets.connect(self.address) as websocket:
            await websocket.send(string)
            message = await websocket.recv()
            decrypted = self.rsa_decrypt(message)
            if decrypted is None:
                return None
            self.response = decrypted
            if len(self.response) != 3:
                return None
            if not ("hash" in self.response.keys()):
                return None
            hash = self.response.get("hash")
            if len(hash) != 32:
                return None
            if self.connection_hash != hash:
                return None
            self.aes = self.response.get("aes_key")
            self.id = self.response.get("client_id")
            self.connected = True
            return "Connected with the server"

    async def get_possible_chatters(self, string: str):
        async with websockets.connect(self.address) as websocket:
            await websocket.send(string)
            message = await websocket.recv()
            if type(message) != str:
                aes = pyaes.AESModeOfOperationCTR(self.aes)
                message = aes.decrypt(message).decode("utf-8")
            if "Error" in message:
                return None
            if len(message) == 0:
                return "There is no available users now"
            list1 = list(message.split(","))
            return list1

    async def send(self, msg):
        async with websockets.connect(self.address) as websocket:
            print(msg)
            await websocket.send(msg)
            resp = await websocket.recv()
            return resp

    def connect_and_chat(self):
            while(True):
                time.sleep(0.25)
                dict1 = {"id": self.id, "method": "get-aes"}
                to_send = json.dumps(dict1)
                message = asyncio.run(self.send(to_send))
                if not( message is None) and message != "No available aes keys!":
                    dictionary1 = json.loads(message)
                    id_1 = dictionary1.get('id')
                    msg_1 = dictionary1.get('msg')
                    msg_1 = msg_1.encode("raw_unicode_escape")
                    person = None
                    for per in self.connected_persons:
                        if per[0] == id_1:
                            person = per
                            break
                    if not(person is None):
                        msg_1 = rsa.decrypt(msg_1, person[2])
                        msg_1 = str(msg_1)
                        msg_1 = msg_1[3:]
                        msg_1 = msg_1[:-2]
                        listt1 = list(msg_1.split(','))
                        listt1 = [int(x) for x in listt1]
                        to_bytes = bytes(listt1)
                        person[3] = to_bytes

                dict1 = {"id": self.id, "method": "get-rsa"}
                to_send = json.dumps(dict1)
                message = asyncio.run(self.send(to_send))
                aes = pyaes.AESModeOfOperationCTR(self.aes)
                message = aes.decrypt(message).decode("utf-8")
                if type(message) == str:
                    if message != "No available rsa keys!":
                        list1 = list(message.split(';'))
                        list1 = [json.loads(x) for x in list1]
                        for a in list1:
                            temp = []
                            temp.append(a.get('from'))
                            temp.append(a.get("rsa").encode("raw_unicode_escape"))
                            temp.append(None)
                            temp.append(os.urandom(32))
                            self.connected_persons.append(temp)
                            rsa1 = temp[1]
                            rsa1 = rsa.key.PublicKey.load_pkcs1(rsa1)
                            list1 = list(temp[3])
                            aes_send = "{"
                            for a in list1:
                                aes_send = aes_send + str(a) + ","
                            aes_send = aes_send[:-1]
                            aes_send += "}"
                            encrypted_key = self.rsa_encrypt2(aes_send, rsa1)
                            dict2 = {"id": self.id,"receiver_id": temp[0],"method": "send-aes",
                                     "msg": encrypted_key.decode("raw_unicode_escape")}
                            asyncio.run(self.send(json.dumps(dict2)))
                dict1 = {"id": self.id, "method": "get-message"}
                to_send = json.dumps(dict1)
                message = asyncio.run(self.send(to_send))
                if message != "No messages":
                    dict1 = json.loads(message)
                    id_1 = dict1.get("id")
                    person = None
                    for per in self.connected_persons:
                        if per[0] == id_1:
                            person = per
                            break
                    if not (person is None):
                        temp = dict1.get("message")
                        aes = pyaes.AESModeOfOperationCTR(person[3])
                        response = str(aes.decrypt(temp).decode("raw_unicode_escape"))
                        self.interface_reference.textEdit.setTextColor(QColor("green"))
                        self.interface_reference.textEdit.append(response)
                msg = self.remove_message()
                if not(msg is None):
                    receiver_id = msg.get_receiver_id()
                    if len(self.connected_persons) > 0:
                        contains = False
                        for a in self.connected_persons:    #0-receiver_id,1- rsa_public_key,2-rsa_private_key,3-aes-key
                            if a[0] == receiver_id:
                                aes_key = a[3]
                                contains = True
                                break
                        if contains is True:
                            if aes_key != "None":
                                aes = pyaes.AESModeOfOperationCTR(aes_key)
                                encrypted = aes.encrypt(msg.get_message())
                                dict = {"from": self.id, "to": receiver_id, "message": encrypted.decode("raw_unicode_escape")}
                                asyncio.run(self.send(json.dumps(dict)))
                            else:
                                self.add_message_on_start(msg)
                        else:
                            temp_list = []
                            (public_key, private_key) = rsa.newkeys(2048, poolsize=8)
                            temp_list.append(receiver_id)
                            temp_list.append(public_key)
                            temp_list.append(private_key)
                            temp_list.append("None")
                            self.connected_persons.append(temp_list)
                            rsa1 = public_key.save_pkcs1("PEM")
                            rsa1 = rsa1.decode("raw_unicode_escape")
                            aes = pyaes.AESModeOfOperationCTR(self.aes)
                            encrypted = aes.encrypt(rsa1)
                            dict1 = {"id": self.id, "receiver_id": receiver_id, "method": "key",
                                     "message": encrypted.decode("raw_unicode_escape")}
                            string = json.dumps(dict1)
                            message = asyncio.run(self.send(string))
                            self.add_message_on_start(msg)
                    else:
                        temp_list = []
                        (public_key, private_key) = rsa.newkeys(2048, poolsize=8)
                        temp_list.append(receiver_id)
                        temp_list.append(public_key)
                        temp_list.append(private_key)
                        temp_list.append("None")
                        self.connected_persons.append(temp_list)
                        rsa1 = public_key.save_pkcs1("PEM")
                        rsa1 = rsa1.decode("raw_unicode_escape")
                        aes = pyaes.AESModeOfOperationCTR(self.aes)
                        encrypted = aes.encrypt(rsa1)
                        dict1 = {"id": self.id, "receiver_id": receiver_id, "method": "key",
                                 "message": encrypted.decode("raw_unicode_escape")}
                        string = json.dumps(dict1)
                        message = asyncio.run(self.send(string))
                        self.add_message_on_start(msg)

    def add_message(self, message):
        self.message_lock.acquire()
        self.messages.append(message)
        self.message_lock.release()

    def add_message_on_start(self, message):
        self.message_lock.acquire()
        self.messages.insert(0, message)
        self.message_lock.release()

    def remove_message(self):
        msg = None
        self.message_lock.acquire()
        if len(self.messages) > 0:
            msg = copy.deepcopy(self.messages[0])
            del self.messages[0]
        self.message_lock.release()
        return msg

    def get_possible_chatters_1(self):
        if self.connected is False:
            return None
        dict2 = {"method": "get"}
        to_encryption = json.dumps(dict2)
        if type(self.aes) != bytes:
            list1 = list(self.aes.split(','))
            list1 = [int(x) for x in list1]
            self.aes = bytes(list1)
        aes = pyaes.AESModeOfOperationCTR(self.aes)
        encrypted = aes.encrypt(to_encryption)

        dict1 = {'id': str(self.id), "message": str(encrypted)}
        string = json.dumps(dict1)
        rt = asyncio.run(self.get_possible_chatters(string))
        return rt

    def start(self, nick: str):
        if self.connected is True:
            return "Error occured"
        (self.public_key, self.private_key) = rsa.newkeys(2048, poolsize=8)
        rsa1 = self.public_key.save_pkcs1("PEM")
        rsa1 = rsa1.decode("utf-8")
        self.connection_hash = self.connection_code + rsa1[:32] + nick
        self.connection_hash = hashlib.md5(self.connection_hash.encode('utf-8')).hexdigest()
        if len(nick) < 5 or len(nick) > 30:
            return "Insert valid nick! Nick has to contain from 5 to 30 characters"
        dict1 = {"method": "hello", "message": {"rsa_key": rsa1, "nick": nick}}
        string = json.dumps(dict1)
        ret = asyncio.run(self.hello(string))
        if ret is None:
            return "Error occured"
        return ret


if __name__ == '__main__':
    freeze_support()
    c = Client()
    c.start()