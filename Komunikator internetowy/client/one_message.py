

class OneMessage:

    def __init__(self, message1, nick, id):
        self.message = message1
        self.receiver_nick = nick
        self.receiver_id = id

    def get_message(self):
        return self.message

    def get_receiver_nick(self):
        return self.receiver_nick

    def get_receiver_id(self):
        return self.receiver_id

