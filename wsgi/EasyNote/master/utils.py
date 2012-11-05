#-*- coding: utf-8 -*-

import os
import pymongo
from datetime import datetime

MONGO_HOST = os.environ['OPENSHIFT_NOSQL_DB_HOST']
MONGO_PORT = int(os.environ['OPENSHIFT_NOSQL_DB_PORT'])
MONGO_USER = os.environ['OPENSHIFT_NOSQL_DB_USERNAME']
MONGO_PASS = os.environ['OPENSHIFT_NOSQL_DB_PASSWORD']

def make_datetime():
    return datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M")

def get_connection():
    db = pymongo.Connection(MONGO_HOST, MONGO_PORT).EasyNote
    db.authenticate(MONGO_USER, MONGO_PASS)
    return db


if __name__ == '__main__':
    conn = get_connection()
