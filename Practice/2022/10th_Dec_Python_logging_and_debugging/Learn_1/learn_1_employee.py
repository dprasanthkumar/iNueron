import logging
import learn_1_saveToFile as STF

# below is the code where we are creating our own loggecd   r
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

fh=logging.FileHandler(filename='adasdasd.log')
fh.setFormatter(f)
logger.addHandler(fh)

#---------------------------------------------------------------------------------

#logging.basicConfig(filename='learn_saveToFile.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

logger.debug('Start of employee program')

name = 'imran'
age = 27
email = 'imran@gmail.com'

if STF.namecheck(name) is True:
    STF.saveData(name,age,email)
else:
    logger.critical('Employee check failed')


logger.debug('End of employee program')
logger.debug('######################')