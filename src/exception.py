import sys
from src.logger import logging


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()  
    #_,_,exc_tb = error_detail.exc_info()# exc_info() returns three things:# (type, value, traceback)
    # Here we only need the traceback, so we store it in exc_tb.

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message    


# Normal Exception → basic error message

# CustomException → file + line number + error message