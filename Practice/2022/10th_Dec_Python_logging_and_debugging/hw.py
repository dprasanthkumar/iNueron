import logging

#logging.basicConfig(level=logging.INFO,filename='addition.log',format='-%(asctime)s -%(filename)s -%(message)s')
logging.basicConfig(level=logging.DEBUG,filename='addition.log',format='-%(asctime)s -%(filename)s -%(message)s')

def addition(*args):
    logging.info('this is my adddition function')
    sum=0
    for i in args:
        logging.info(str(i))
        
        sum=sum+i
    logging.debug(sum)
    r=print(sum)
        

    return sum


addition(1,2,3,4,5,6,7)