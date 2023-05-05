import copy
import json
from threading import Lock


class Connection():

    def __init__(self, c_from, c_to, c_rsa):
        self.sender = c_from
        self.receiver = c_to
        self.connection_rsa = c_rsa
        self.done = False
        self.done2 = False
        self.added = False
        self.aes_messages = []
        self.lock = Lock()

    def set_added(self):
        self.added = True

    def get_added(self):
        return self.added

    def set_done(self):
        self.done = True

    def get_done(self):
        return self.done

    def set_done2(self, parameter):
        self.done2 = parameter

    def get_done2(self):
        return self.done2

    def add_aes_message(self, message):
        self.lock.acquire()
        self.aes_messages.append(message)
        self.lock.release()

    def pop_aes_messages(self):
        messages = None
        self.lock.acquire()
        messages = copy.deepcopy(self.aes_messages)
        self.aes_messages.clear()
        self.lock.release()
        return messages
    def get_sender(self):
        return self.sender

    def get_receiver(self):
        return self.receiver

    def get_rsa(self):
        return self.connection_rsa

    def to_string(self):
        dict ={"from": self.sender,"to": self.receiver, "rsa": self.connection_rsa.decode("raw_unicode_escape")}
        return json.dumps(dict)
