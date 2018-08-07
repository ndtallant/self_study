# Built in!
import logging
# https://12factor.net/logs 

# The Basics, logger | handler | formatter
logger = logging.getLogger()

handler = logging.StreamHandler()

formatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)
# Level is set to warning by default, so you 
# can't see info or debug. Setting to debug will work
logger.setLevel(logging.DEBUG)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    x = 5
    y = 3
    add(x, y)
    logger.warning('Uh oh I\'m adding')
    logger.info('but this is info')
    subtract(x, y)
    logger.info('all done')
