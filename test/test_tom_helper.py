from logic import TomHelper, WsConnection, TomHelper
from models import Block
from models import Response
import unittest
import random

class TestTomHelper(unittest.TestCase):
    
    __ws_connection =  WsConnection("209.126.82.146", 8080, 0.11)
    __tom_helper = TomHelper(__ws_connection, Response(), Block())
    
    def test_response_varibale(self):
        response = { 'a': 1542, 'b': 18}
        self.assertAlmostEqual(self.__tom_helper.set_response_variables(response), [1542, 18] )
    
    def test_block(self):
        self.test_response_varibale()
        responses = [ Response(2, 3), Response(3,3123), Response(5,3123),
                    Response(22,1233), Response(31,8643), Response(2,65434) ]
        self.__tom_helper.set_responses_list(responses)
        self.assertAlmostEqual(self.__tom_helper.find_b_list(2), [3, 65434] )

if __name__ == '__main__':
    unittest.main()