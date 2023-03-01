# -------------
# |  logging  |
# -------------

import logging
from datetime import datetime

now = datetime.now()
 
# dd/mm/YY H:M:S
# logs of each runs are separated
log_file_name = now.strftime("%d-%m-%Y_%H-%M-%S")

logging.basicConfig(filename="logs/{}.log".format(log_file_name),
                        level=logging.INFO,
                        format='[%(filename)s] '    
                                '[%(levelname)s] '
                                '[%(funcName)s()] '
                                '[%(lineno)d]\t'
                                '%(message)s')
