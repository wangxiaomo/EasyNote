#-*- coding: utf-8 -*-

import os
import pymongo
from datetime import datetime

def make_datetime():
    return datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M")

def get_connection():
    db = pymongo.Connection(os.environ['OPENSHIFT_NOSQL_DB_URL']).EasyNote
    return db

if __name__ == '__main__':
    print make_datetime()
