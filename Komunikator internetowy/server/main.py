import asyncio
import websockets
from clients.clients import Clients as cls
from checker import Checker as c
from tasks_executor import TasksExecutor as te

class Start:
    def __init__(self):
        self.clients = cls()
        self.start_server = None
        self.checker = c()
        self.tasks_executor = te(self.clients)
        self.ip = "localhost"
        self.port = 7777
        with open("config.txt","r") as f:
            a = f.read().splitlines()
            self.ip = a[0]
            self.port = int(a[1])

        self.run_server()

    async def handler(self, websocket, path):
        data = await websocket.recv()
        print("------------------request------------------")
        print(data)
        dictionary = self.checker.check(data)
        response = "Error. Bad request"
        if not (dictionary is None):
            response = self.tasks_executor.execute(dictionary, data)
            if response is None:
                response = "Error. Bad request"
        print("------------------response------------------")
        print(response)
        await websocket.send(response)

    def run_server(self):
        self.start_server = websockets.serve(self.handler, self.ip, self.port)
        asyncio.get_event_loop().run_until_complete(self.start_server)
        asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    Start()
