#-*- coding: utf-8 -*-


import pymongo
from datetime import datetime

HOST = '127.9.112.129'
PORT = '27017'

def make_datetime():
    return datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M")

def get_connection():
    try:
        return pymongo.Connection(HOST, int(PORT)).EasyNote
    except:
        return pymongo.Connection('localhost', int(PORT)).EasyNote


if __name__ == '__main__':
    conn = get_connection()
