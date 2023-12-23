import logging

logging.basicConfig(filename='namecheck_1.log',level=logging.DEBUG)

def namecheck(name):
    if len(name) < 2:
        logging.debug('Chech for the name length')
        return 'invalid name'
    elif name.isspace():
        logging.debug('Cheking for name has space')
        return 'invalid name'
    elif name.isalpha():
        logging.debug('Cheking for name has alphabet')
        return 'valid name'
    elif name.replace(' ','').isalpha():
        logging.debug('checking for full name')
        return 'name is valid'
    else:
        logging.debug('Failed all checkes')
        return 'invalid name'
    
name=namecheck('Prasanth')
print(name)