# -*- coding:utf-8 -*-
import json
import logging
import sys
import os

from kafka import KafkaProducer
from kafka.errors import KafkaError
from datetime import datetime
from logconfs.json_formatter import JSONFormatter
from logconfs.con_vars import conf


class KafkaLoggingHandler(logging.Handler):
    """
    自定义handler,发送消息至elk
    """
    def __init__(self):
        logging.Handler.__init__(self)
        self.kafkatopic = conf['elk']['topic']
        elk_nodes = [server for server in conf['elk']['server'].split(',')]
        self.producer = KafkaProducer(bootstrap_servers=elk_nodes)

    def emit(self, record):
        try:
            msg_str = self.format(record)
            # msg = json.loads(msg_str.replace("\'", "\""))
            # parmas_message = json.dumps(msg, ensure_ascii=False)
            producer = self.producer
            producer.send(self.kafkatopic, value=msg_str.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print(e)

    def close(self):
        # self.producer.stop()
        logging.Handler.close(self)

