import logging as log
import os

#SECTION - Get the script's directory
script_dir = os.path.dirname(__file__)

#SECTION - Create the log directory if it doesn't exist
log_dir = os.path.join(script_dir, 'log')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

#SECTION - Specify the full path to the log file
log_file = os.path.join(log_dir, 'my_logs.log')

log.basicConfig(filename=log_file, 
                encoding='utf-8', 
                filemode='w', 
                level=log.DEBUG ,
                #filename='my_logs.log' , 
                #filemode='w'
                )

log.debug('DEBUG')
log.info('INFO')
log.warning('WARNING')
log.error('ERROR')
log.critical('CRITICAL')