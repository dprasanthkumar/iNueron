import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

def add(x,y):
    return x+y
def product(x,y):
    return x*y
def susstarct(x,y):
    return x-y

num_1=10
num_2=3

add_result=add(num_1,num_2)
#logging.debug(add_result)
logging.debug(add_result)
product_result=product(num_1,num_2)
#logging.debug(product_result)
logging.info(product_result)
susstarct_result=susstarct(num_1,num_2)
#logging.debug(susstarct_result)
logging.warning(susstarct_result)