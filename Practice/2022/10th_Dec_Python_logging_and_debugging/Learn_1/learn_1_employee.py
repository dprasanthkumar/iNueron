import logging
import learn_1_saveToFile as STF

# below is the code where we are creating our own logger
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

fh=logging.FileHandler(filename='learn_saveToFile.log')
fh.setFormatter(f)
logger.addHandler(fh)

#---------------------------------------------------------------------------------

#logging.basicConfig(filename='learn_saveToFile.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

logging.debug('Start of employee program')

name = 'imran'
age = 27
email = 'imran@gmail.com'

if STF.namecheck(name) is True:
    STF.saveData(name,age,email)
else:
    logging.critical('Employee check failed')


logging.debug('End of employee program')
logging.debug('######################')