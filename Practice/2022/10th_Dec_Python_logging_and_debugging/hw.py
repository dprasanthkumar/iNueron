import logging

logging.basicConfig(filename='addition.log',level=logging.DEBUG)

def addition(*args):
    logging.info('this is my adddition function')
    sum=0
    for i in args:
        logging.info(str(i))
        sum=sum+i
    return sum

f=open('addition.log','r')
print(f.read())
addition(1,2,3,4,5,6,7)