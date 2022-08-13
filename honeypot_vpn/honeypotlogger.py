import datetime
import logging
import logging.config
from os import path
from datetime import datetime
import sys
import logstash

class HoneypotLogger:

    def __init__(self, args):
        self.args = args

    def configureLogger(self, writeFileLogs = True, sendToElasticSearch = False,  logstashHost = 'localhost:5000'):
        log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logger.cfg')
        #logging.config.fileConfig(log_file_path)
        logger = logging.getLogger('HoneypotVPNLogger')
        logger.setLevel(logging.DEBUG)
        if sendToElasticSearch:
            logstashHost = logstashHost.replace("http://","")
            logstashHost = logstashHost.replace("https://","")
            logstashconf = logstashHost.split(":")
            logger.addHandler(logstash.TCPLogstashHandler(logstashconf[0], int(logstashconf[1]), version=1))
            extra = {
                'elastic_fields': {
                    'version': 'python version: ' + repr(sys.version_info)
                }
            }
            logger.info("Logger was configured", extra=extra)
        if writeFileLogs: 
            fh = logging.FileHandler(path.join(path.dirname(path.abspath(__file__)), 'logs/{:%Y-%m-%d}.log'.format(datetime.now())), mode='a')
            formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            logger.info('WRITING LOG FILE:' + path.join(path.dirname(path.abspath(__file__)), 'logs/{:%Y-%m-%d}.log'.format(datetime.now())))

        print("configuredddddd...")

