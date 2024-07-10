import logging as log
import os

log.logging.basicConfig(level=log.logging.DEBUG)


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
log.logging.info('The answer is: %s' , x)
log.logging.info(f'The answer is: {x}')