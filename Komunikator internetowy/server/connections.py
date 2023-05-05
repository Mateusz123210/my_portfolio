import copy
from threading import Lock
from connection import Connection


class Connections:

    def __init__(self):
        self.lock = Lock()
        self.connection_list = []


    def check_and_add_connection(self,c_from, c_to, c_rsa):
        self.lock.acquire()
        b = None
        for a in self.connection_list:
            if (a.get_sender() == c_from and a.get_receiver() == c_to) or (a.get_sender() == c_to and a.get_receiver() == c_from):
                self.lock.release()
                return None

        c = Connection(c_from, c_to, c_rsa)
        self.connection_list.append(c)
        self.lock.release()
        return "Waiting for receiver"

    def get_connections(self, c_to):
        b = []
        self.lock.acquire()
        for a in range(len(self.connection_list)):
            if self.connection_list[a].get_receiver() == c_to and self.connection_list[a].get_done() == False:
                b.append(self.connection_list[a])
                self.connection_list[a].set_done()
        self.lock.release()
        return b

    def get_connections_senders(self, c_from):
        b = []
        self.lock.acquire()
        for a in range(len(self.connection_list)):

            if self.connection_list[a].get_sender() == c_from and self.connection_list[a].get_done2() == False and self.connection_list[a].get_added() is True:
                b.append(self.connection_list[a])
                self.connection_list[a].set_done2(True)
        self.lock.release()
        return b

    def get_connection(self,c_from, c_to):
        b = None
        self.lock.acquire()
        for a in self.connection_list:
            if (a.get_sender() == c_from and a.get_receiver() == c_to) or (a.get_sender() == c_to and a.get_receiver() == c_from):
                b = a
                a.set_done2(False)
                a.set_added()
                break
        self.lock.release()
        return b