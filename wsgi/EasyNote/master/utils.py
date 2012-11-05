#-*- coding: utf-8 -*-

import os
import pymongo
from datetime import datetime,timedelta
from dateutil import tz

def make_datetime():
    utc = tz.gettz('UTC')
    utc_now = datetime.utcnow()
    cst_now = utc_now + timedelta(hours=8)
    return datetime.strftime(cst_now, "%Y/%m/%d %H:%M")

def get_connection():
    db = pymongo.Connection(os.environ['OPENSHIFT_NOSQL_DB_URL']).EasyNote
    return db

if __name__ == '__main__':
    print make_datetime()
