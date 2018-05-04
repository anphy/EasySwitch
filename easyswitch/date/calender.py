#coding: utf-8
__author__ = "anphyLong"
__date__   = " 2018/05/04"

'''
functions which are mostly connected to chinese calender
'''

import datetime

__all__ = ["is_vocation_or_weekend", "days_before_today", "yield_days_before"]

vocations = {
    "2018-01-01",
    "2018-02-15",
    "2018-02-16",
    "2018-02-17",
    "2018-02-18",
    "2018-02-19",
    "2018-02-20",
    "2018-02-21",
    "2018-04-29",
    "2018-04-30",
    "2018-05-01",
    "2018-06-18",
    "2018-09-24",
    "2018-10-01",
    "2018-10-02",
    "2018-10-03",
    "2018-10-04",
    "2018-10-05",
    "2018-10-06",
    "2018-10-07"
}

def is_vocation_or_weekend(date=None):
    '''
    return True if it is vocation or weekend
    '''
    thisD = date or datetime.date.today()
    return str(thisD) in vocations or thisD.weekday() > 4


def days_before_today(days=1):
    '''
    return date that is days before today exclude the vocation and weekend
    '''
    startdate = datetime.date.today()
    while days:
        startdate -= datetime.timedelta(days=1)
        while is_vocation_or_weekend(startdate):
            startdate -= datetime.timedelta(days=1)
        days -= 1
    return startdate


def yield_days_before(days=1):
    '''
    As hinted by it's name, this function yield all days valid until the farest day
    '''
    startdate = datetime.date.today()
    while days:
        startdate -= datetime.timedelta(days=1)
        while is_vocation_or_weekend(startdate):
            startdate -= datetime.timedelta(days=1)
        days -= 1
        yield startdate
