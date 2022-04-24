import unittest
from logic import WsConnection

class TestWsConnection(unittest.TestCase):
    
    
    async def test_ws_connection(self):
        ws_connection =  WsConnection("209.126.82.146", 8080, 0.11)
        response = await ws_connection.get_response()
        self.assertIsInstance(response, dict)
        
if __name__ == '__main__':
    unittest.main()