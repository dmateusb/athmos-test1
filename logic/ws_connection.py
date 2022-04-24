import websocket
import json
from models.meta.singleton import Singleton

class WsConnection(metaclass=Singleton):

    def connect(self):
        url = "ws://{}:{}".format(self.__path, self.__port)
        self.__ws.connect(url, close_timeout=self.__close_timeout)
        

    async def get_response(self):
        return json.loads(self.__ws.recv())
        
    def get_path(self):
        return self.__path
    
    def set_path(self, path):
        self.__path = path
        
    def set_port(self, port):
        self.__port = port
        
    def set_close_timeout(self, close_timeout):
        self.__close_timeout = close_timeout
        
    def set_ws(self, ws):
        self.__ws = ws
    
    def get_path(self):
        return self.__path
        
    def get_port(self):
        return self.__port
        
    def get_close_timeout(self):
        return self.__close_timeout
        
    def get_ws(self):
        return self.__ws

    def __init__(self, path, port, close_timeout):
        self.__path = path
        self.__port = port
        self.__close_timeout = close_timeout
        self.__ws = websocket.WebSocket()
        self.connect()