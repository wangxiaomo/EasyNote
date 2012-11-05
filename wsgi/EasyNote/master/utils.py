#-*- coding: utf-8 -*-

import os
import pymongo
from datetime import datetime

HOST = os.environ['OPENSHIFT_DB_HOST']
PORT = os.environ['OPENSHIFT_DB_PORT']

def make_datetime():
    return datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M")

def get_connection():
    try:
        return pymongo.Connection(HOST, int(PORT)).EasyNote
    except:
        assert False, "connection Error"
        return pymongo.Connection('localhost', int(PORT)).EasyNote


if __name__ == '__main__':
    conn = get_connection()
