#-*- coding: utf-8 -*-

import os
import pymongo
from datetime import datetime

MONGO_HOST = '127.9.112.129'
MONGO_PORT = 27017

def make_datetime():
    return datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M")

def get_connection():
    db = pymongo.Connection(MONGO_HOST, MONGO_PORT).EasyNote
    return db


if __name__ == '__main__':
    conn = get_connection()
