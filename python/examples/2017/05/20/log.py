# -*- coding: UTF-8 -*-
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)-5s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M')

logging.info("info message.")
logging.debug("debug message.")
logging.error("error message.")