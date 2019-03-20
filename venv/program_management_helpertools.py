import numpy as np

import datetime


def get_start_data_from_calendar_week(year, calendar_week):
    '''Solution from Ron on stackoverflow
       https://stackoverflow.com/questions/51194745/get-first-and-last-day-of-given-week-number-in-python
    '''
    monday = datetime.datetime.strptime(f'{year}--{calendar_week}--1', "%Y-%W-%w").date()
    return monday


def get_week_number_from_isodate(year, month, day):
    wk_number = datetime.date(year, month, day).isocalendar()[1]
    return wk_number

def get_num_of_wks_btwn_dates(start_date, end_date):
    num_weeks = (end_date - start_date).weeks
    return num_wks

def convert_date_str_into_datetime_obj(date, format='%Y-%m-%d'):
    return datetime.datetime.strptime(date, format)

def get_current_date():
    return datetime.datetime.now()