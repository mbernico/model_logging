import unittest
from io import StringIO
from mock import patch
from model_logger import Borg, BaseLogger, EndpointLogger
import logging
import sys


class TestModelLogger(unittest.TestCase):

    def test_Borg(self):
        b1 = Borg()
        b2 = Borg()
        self.assertTrue(b1 != b2)
        b1.sound = "woof"
        self.assertTrue(b2.sound == "woof")

    def test_BaseLoggerBorginess(self):
        logger = BaseLogger()
        logger2 = BaseLogger()
        self.assertTrue(id(logger.logger) == id(logger2.logger))

    # @patch('sys.stdout', new_callable=StringIO)
def test_EndpointLoggerLog(capsys):
    logger = EndpointLogger(model_name="test_model", model_version="0")
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.logger.addHandler(stdout_handler)
    # patch requires a new stdout handler, don't know why

    logger.log(inputs={'a':1, 'b':2}, outputs={'answer':2}, return_code=200, caller="maybe")
    out, err = capsys.readouterr()
    print("captured is " + str(out))
    assert "model_name" in out
    #assert '{"time":2018-05-05 15:30:53 -0500,"model_name":test_model,"model_version":0,"delta_time":-1,' \
    #       '"inputs":{"a": 1, "b": 2},"outputs":{"answer": 2},"return_code":200, "caller":maybe}' == captured[0]
