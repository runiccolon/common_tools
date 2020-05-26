# -*- coding:utf-8 -*-

import logging.config
import os
from logconfs.con_vars import conf

log_conf_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), conf['log_config']['file'])
logging.config.fileConfig(log_conf_file_path)
