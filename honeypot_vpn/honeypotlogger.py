import datetime
import logging
import logging.config
from os import path
from datetime import datetime
import sys
import logstash
import platform
import os
import socket
import time

class HoneypotLogger:

    def __init__(self, args):
        self.args = args
        
    
    def wait_for_logstash_connection(self,ip,port):
        maxattempts = 60
        attempt = 0
        logger = logging.getLogger('HoneypotVPNLogger')
        logger.setLevel(logging.DEBUG)
        while True:
            try:
                attempt = attempt + 1
                if attempt > maxattempts:
                    logger.info("Can't connect to Logstash at " + ip +":"+ str(port) + " -> Max attempts reached:" + str(maxattempts))
                    return
                time.sleep(5)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(5.0)
                result = sock.connect_ex((ip,port))
                if result == 0:
                    logger.info("Logstash connected to " + ip +":"+ str(port) + " -> Attempt:" + str(attempt))
                    return
                logger.info("Waiting for logstash service up at " + ip +":"+ str(port) + " -> Attempt:" + str(attempt))
            except socket.error as e:
                logger.info(e)
                pass

    def configureLogger(self, writeFileLogs = True, sendToElasticSearch = False,  logstashHost = 'localhost:5000', folderLogs="/honeypotvpn/logs"):
    	
        log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logger.cfg')
        if not os.path.exists(folderLogs):
            os.makedirs(folderLogs)
        logger = logging.getLogger('HoneypotVPNLogger')
        logger.setLevel(logging.DEBUG)
        if writeFileLogs: 
            fh = logging.FileHandler(folderLogs+ '/{:%Y-%m-%d}.log'.format(datetime.now()), mode='a')
            formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            logger.info('WRITING LOG FILE:' + folderLogs + '/{:%Y-%m-%d}.log'.format(datetime.now()))
        if sendToElasticSearch:
            logstashHost = logstashHost.replace("http://","")
            logstashHost = logstashHost.replace("https://","")
            logstashconf = logstashHost.split(":")
            self.wait_for_logstash_connection(logstashconf[0], int(logstashconf[1]))
            logger.addHandler(logstash.TCPLogstashHandler(logstashconf[0], int(logstashconf[1]), version=1))
            extra = {
                'elastic_fields': {
                    'version': 'python version: ' + repr(sys.version_info)
                }
            }
            logger.info("Logger was configured", extra=extra)
        else:
            logging.config.fileConfig(log_file_path)


        print("configuredddddd...")

