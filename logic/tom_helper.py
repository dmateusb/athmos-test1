import copy
import time
import os


class TomHelper():
    
    def set_response_variables(self, response):
        new_instance = self.__response.__class__(response['a'], response['b'])
        self.__response = new_instance
        return [self.__response.get_a(), self.__response.get_b()]
        
    def find_b_list(self, i):
        return [ response.get_b() for response in self.__responses_list if response.get_a() == i ]

    
    def create_block(self, index):
        b_list = self.find_b_list(index)
        self.__block.set_a(index)
        self.__block.set_b_list(b_list)   
        return self.__block.set_b_list(b_list)
        
    def make_summary(self):
        for i in range(1, 101):
            self.create_block(i)
            print(self.__block)
        
    async def get_responses(self):
        for i in range(100): 
            response = await self.__ws_connection.get_response()
            self.set_response_variables(response)
            self.__responses_list.append(copy.copy(self.__response))
        return self.__responses_list
        
    async def start(self):
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        cont = 0 
        while True:
            await self.get_responses()
            if cont == 0: print("Recibiendo Datos...\n")
            cont += 1
            if cont == 600:
                clearConsole()
                cont = 0
                self.make_summary()
                self.__responses_list = []
            time.sleep(0.1)
        
    async def __call__(self):
        await self.start()
        
    def get_ws_connection(self):
        return self.__ws_connection
        
    def get_response(self):
        return self.__response
        
    def get_responses_list(self):
        return self.__responses_list
        
    def get_block(self):
        return self.__block
        
    def set_ws_connection(self, ws_connection):
        self.__ws_connection = ws_connection
        
    def set_response(self, response):
        self.__response = response
        
    def set_responses_list(self, __responses_list):
        self.__responses_list = __responses_list
        
    def set_block(self, block):
        self.__block = block
    
    def __init__(self, ws_connection, response, block):
        self.__ws_connection = ws_connection
        self.__response = response
        self.__block = block
        self.__responses_list = []
