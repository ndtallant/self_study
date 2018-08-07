# Built in!
import logging
# https://12factor.net/logs 

# The Basics, logger | handler | formatter
logger = logging.getLogger()

# This has to come before other logging calls / options

logging.basicConfig(filename='example.log'
        , filemode='w' # This rewrites the file each time
        , level=logging.DEBUG)

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
