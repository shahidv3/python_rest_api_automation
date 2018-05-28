import logging



def log_level():
    ''' setting the log level to DEBUG '''
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info('Start api tests')
    logger.debug('Records: %s', input)