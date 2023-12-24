import logging
import learn_SaveToFile as STF


logging.basicConfig(filename='learn_saveToFile.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')



#logging.basicConfig(filename='employee.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
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