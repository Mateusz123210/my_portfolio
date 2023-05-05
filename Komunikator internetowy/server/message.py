import json


class Message:

    def __init__(self, sender_id, receiver_id, message):
        self.id = sender_id
        self. receiver_id = receiver_id
        self.message = message

    def get_message(self):
        return self.message

    def get_sender_id(self):
        return self.id

    def get_receiver_id(self):
        return self.receiver_id

    def to_json_string(self):
        dict1 = {"id": self.id,"receiver_id": self.receiver_id,"message": self.message}
        return json.dumps(dict1)



