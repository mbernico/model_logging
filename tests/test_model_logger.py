import logging
import sys
import time
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model_logger import *


def test_Borg():
    b1 = Borg()
    b2 = Borg()
    assert b1 != b2
    b1.sound = "woof"
    assert b2.sound == "woof"


def test_BaseLoggerBorginess():
    logger = BaseLogger()
    logger2 = BaseLogger()
    assert id(logger.logger) == id(logger2.logger)


def test_EndpointLoggerLog(capsys):
    logger = EndpointLogger(model_name="test_model", model_version="0")
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.logger.addHandler(stdout_handler)
    logger.log(inputs={'a':1, 'b':2}, outputs={'answer':2}, return_code=200, caller="maybe")
    out, err = capsys.readouterr()
    assert "model_version" in out


def test_timer():
    logger = EndpointLogger(model_name="test_model", model_version="0")
    logger.start_timer()
    time.sleep(1)
    time_out = logger.get_elapsed_time()
    assert time_out > 0


def test_current_time():
    logger = EndpointLogger(model_name="test_model", model_version="0")
    current_time = logger.get_current_time(human=True)
    assert ":" in current_time
    current_time = logger.get_current_time(human=False)
    assert current_time > 0



