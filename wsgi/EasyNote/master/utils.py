#-*- coding: utf-8 -*-

import os
import pymongo
from datetime import datetime
from dateutil import tz

def make_datetime():
    utc = tz.gettz('UTC')
    cst = tz.gettz('CST')
    utc_now = datetime.utcnow().replace(tzinfo=utc)
    cst_date = utc_now.astimezone(cst)
    return datetime.strftime(cst_date, "%Y/%m/%d %H:%M")

def get_connection():
    db = pymongo.Connection(os.environ['OPENSHIFT_NOSQL_DB_URL']).EasyNote
    return db

if __name__ == '__main__':
    print make_datetime()
