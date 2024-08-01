# error.py, The python-file
import _pyerror
import matplotlib

__all__ = ["Error"]

class Error(_pyerror.Error):
    def __init__(self):
        super().__init__()

    def error2(self):
        print("Error from Python")
        return super().error()