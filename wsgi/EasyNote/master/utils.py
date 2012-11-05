#-*- coding: utf-8 -*-

import os
import pymongo
from datetime import datetime

def make_datetime():
    return datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M")

def get_connection():
    return pymongo.Connection().EasyNote


if __name__ == '__main__':
    conn = get_connection()
