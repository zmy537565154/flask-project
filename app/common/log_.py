import logging
import time
import os
import sys

# 日志管理
logger = logging.getLogger('logger')
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s \n')
try:
    file_handler = logging.FileHandler(
        'logs/{}.log'.format(time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))))
except:
    os.mkdir('logs')
    file_handler = logging.FileHandler(
        'logs/{}.log'.format(time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))))
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter

logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)