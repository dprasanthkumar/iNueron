import logging

#logging.basicConfig(level=logging.INFO,filename='addition.log',format='-%(asctime)s -%(filename)s -%(message)s')
logging.basicConfig(level=logging.DEBUG,filename='addition_1.log',format='-%(asctime)s -%(filename)s -%(message)s')

def addition(*args):
    logging.info('this is my adddition function')
    #logging.info(str(args))
    logging.debug(sum(args))
    
    return sum(args)


addition(1,2,3,4,5,6,7)