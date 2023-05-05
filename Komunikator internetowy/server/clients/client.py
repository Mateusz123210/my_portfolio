import copy
from threading import Lock


class Client:

    def __init__(self, rsa_key, client_id, nick):
        self.rsa_key = rsa_key
        self.id = client_id
        self.nick = nick
        self.aes_key = None
        self.message_list = []
        self.hash = None
        self.lock = Lock()


    def set_hash(self, hash_code):
        self.hash = hash_code

    def get_hash(self):
        return self.hash

    def add_message(self,message):
        self.lock.acquire()
        self.message_list.append(message)
        self.lock.release()

    def get_messages(self):
        ret = []
        self.lock.acquire()
        if len(self.message_list) > 0:
            ret = copy.deepcopy(self.message_list)
            self.message_list.clear()
        self.lock.release()
        return ret

    def set_aes_key(self, aes_key):
        self.aes_key = aes_key

    def get_nick(self):
        return self.nick

    def get_id(self):
        return self.id

    def get_rsa_key(self):
        return self.rsa_key

    def get_aes_key(self):
        return copy.deepcopy(self.aes_key)

