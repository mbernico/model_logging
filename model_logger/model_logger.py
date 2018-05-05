import logging
import sys
import json


class Borg:
    """Borg Pattern by  Alex Martelli.  Like a Singleton but maybe more elegant, all instances of this
    class will have the same internal state"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class BaseLogger(Borg):

    def __init__(self):
        Borg.__init__(self)
        if not hasattr(self, 'logger'):  # create a monostate logger only the first time the class is instantiated
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.INFO)
            self.stdout_handler = logging.StreamHandler(sys.stdout)
            self.logger.addHandler(self.stdout_handler)



class EndpointLogger(BaseLogger):

    def __init__(self, model_name, model_version):
        super().__init__()
        self.model_name = model_name
        self.model_version = model_version
        fmt = logging.Formatter('{"time":%(asctime)s,"model_name":%(model_name)s,"model_version":%(model_version)s,'
                                '"delta_time":%(delta_time)s,"inputs":%(inputs)s,"outputs":%(outputs)s,'
                                '"return_code":%(return_code)d, "caller":%(caller)s}', datefmt="%Y-%m-%d %H:%M:%S %z")
        self.stdout_handler.setFormatter(fmt=fmt)
        self.logger.addHandler(self.stdout_handler)

    def log(self, inputs, outputs, return_code, caller):
        # self.logger.info("Log!  %s, %s, %s", self.model_name, self.model_version, inputs)
        self.logger.info(msg="test", extra={"model_name":self.model_name, "model_version":self.model_version, "delta_time":-1,
                         "inputs":inputs, "outputs":outputs, "return_code":return_code, "caller":caller})


