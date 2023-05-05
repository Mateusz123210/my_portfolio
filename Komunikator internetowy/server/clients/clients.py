from threading import Lock
from clients.client import Client as cl
import random
import os
import hashlib
import rsa
import json


class Clients:

    def __init__(self):
        self.client_list = []
        self.lock = Lock()
        self.client_list_size = 0
        self.max_clients = 50
        self.connection_code = '2432001057066268503415301041693135315399706163881527379982899547'
        self. hash = None

    def mutex_unlock(self):
        self.lock.release()

    def get_clients_list_without_release(self):
        self.lock.acquire()
        return self.client_list

    def add_to_clients_list(self, nick: str, client_rsa):
        self.lock.acquire()
        ret = None
        if self.client_list_size < self.max_clients:
            contains = False
            for i in self.client_list:
                if i.get_nick() == nick:
                    contains = True
                    break
            if contains is True:
                ret = "Nick zajety! Wpisz inny."
            else:
                while True:
                    id = random.randint(1, 10000 * self.max_clients)
                    contains = False
                    for i in self.client_list:
                        if i.get_id() == id:
                            contains = True
                            break
                    if contains is False:
                        break
                client = cl(client_rsa, str(id), nick)
                aes_key = os.urandom(32)
                while True:
                    contains = False
                    for i in self.client_list:
                        if i.get_aes_key() == aes_key:
                            contains = True
                            break
                    if contains is False:
                        break
                client.set_aes_key(aes_key)
                list1 = list(client.get_aes_key())

                rsa1 = client.get_rsa_key()
                to_hash = self.connection_code
                for i in range(32):
                    to_hash += rsa1[i]
                to_hash += nick
                hashed = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
                client.set_hash(hashed)
                self.client_list.append(client)
                self.client_list_size += 1
                aes_send = ""
                for a in list1:
                    aes_send = aes_send + str(a) + ","
                aes_send = aes_send[:-1]
                resp = {"aes_key": aes_send, "client_id": str(client.get_id()), "hash": hashed}
                self.lock.release()
                to_encode = json.dumps(resp)
                rsa1 = rsa1.encode("utf-8")
                rsa1 = rsa.key.PublicKey.load_pkcs1(rsa1)
                ret = self.rsa_encrypt(to_encode, rsa1)
        else:
            self.lock.release()

        return ret

    def rsa_encrypt(self, string, key):
        result = []
        for n in range(0, len(string), 245):
            part = string[n:n + 245]
            result.append(rsa.encrypt(part.encode("utf-8"), key))
        return b''.join(result)

    def remove_from_clients_list(self, client):
        self.client_list.remove(client)

