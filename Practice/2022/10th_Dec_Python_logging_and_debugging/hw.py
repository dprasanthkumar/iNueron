import logging

logging.basicConfig(level=logging.DEBUG)

def sum(*args):
    logging.debug(sum(args))
    return sum(args)

sum(1,2)