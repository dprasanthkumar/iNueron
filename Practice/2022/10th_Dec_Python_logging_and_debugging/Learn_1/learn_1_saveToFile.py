
import os
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

fh=logging.FileHandler('adasdasd.log')
fh.setFormatter(f)

logger.addHandler(fh)


#logging.basicConfig(filename='saveTofile.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')


def namecheck(name):
    logger.debug(f'checking name "{name}"....')
    if os.path.exists('data.txt'):
        with open('data.txt','r') as readFile:
            for line in readFile:
                if line.lower().startswith(f'name: {name.lower()}'):
                    logger.error(f'Name: "{name}" already exists')
                    return False
            if len(name) == 0:
                logger.critical('Name cannot be blank')
                return False
            elif not name.isalpha():
                logging.critical('name must be an alphabet')
                return False
            else:
                logging.error(f'check successfull')
                return True
    else:
        logging.debug('No data found')
        return True


def saveData(name,age,email):
    logging.debug(f'Saving details of {name}...')
    with open('data.txt','a') as appendFile:
        appendFile.write(f'Name: {name} - Age: {age} - Email: {email}\n')
        print(f'Details saved successfully')

logging.info('End of saveToFile Program')
logging.debug('########################')
