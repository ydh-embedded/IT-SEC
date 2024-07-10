import logging as log
import os

log.basicConfig(level=log.DEBUG)


#SECTION - Get the script's directory
script_dir = os.path.dirname(__file__)


#SECTION - Create the log directory if it doesn't exist
log_dir = os.path.join(script_dir, 'log')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

#SECTION - Specify the full path to the log file
log_file = os.path.join(log_dir, 'calc_logs.log')


#SECTION - Calc
x: int = 10 + 10
log.info('The answer is: %s' , x)
log.info(f'The answer is: {x}')

#LINK - https://docs.python.org/3/library/logging.html#logrecord-attributes
#SECTION - format
log.basicConfig(format='%(levelname)s (%(asctime)s): %(message)s (Line: %(Lineno)d [%(filename)s])'  ,
                datefmt= '%d/%m/%Y %I:%M:%S: %p',
                level=log.DEBUG)

log.info('Hello, my name is Slim Shady!')
log.warning('Warning, you caught me!')


