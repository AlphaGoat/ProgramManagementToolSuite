import pandas as pd
import numpy as np
import datetime

import os
import argparse


month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
               'Sep','Oct','Nov','Dec']



class Labor(object):

    def __init__(self, name,
                 contract='contract_00',
                 projects=['project_0', 'project_1', 'project_2', 'project_3'],
                 hourly_rate=100,
                 labor_csv_path="~/generic_path/"):
        self.name = name
        self.contract = contract
        self.projects = projects
        self.hourly_rate = hourly_rate
        self.labor_csv_path = labor_csv_path
        for _,_,files in os.walk(self.labor_csv_path):
            if name + '.csv' in files:
                labor_dataframe = self.load_dataframe(labor_csv_path + name + '.csv')
            else:
                labor_dataframe = generate_labor_dataframe()

    def generate_empty_labor_dataframe(self):
        project_hours = dict()
        wk_numbers = range(52)
        current_year = datetime.datetime.now().year
        rows = []
        for wk_number in wk_numbers:
            monday = get_start_data_from_calendar_week(current_year, wk_number)
            rows.append(monday)

        columns = []
        for project in projects:
            projected = project + '_estimated'
            actuals = project + '_actuals'
            columns.append(projected)
            columns.append(actuals)

        labor_dataframe = pd.DataFrame(0, index=rows, columns=columns)

    def insert_project_hours(self, project, hours, date=datetime.datetime.now(),
                                estimated=True):
        year = date.year
        month = date.month
        day = date.day
        wk_number =  get_week_number_from_isodate(year, month, day)
        monday = get_start_data_from_calendar_week(year, wk_number)
        if estimated:
            column = project + '_estimated'
        else:
            column = project + '_actuals'
        df.iloc[monday, column] = hours
        return

    def load_dataframe(self, load_path):
       return pd.read_csv(load_path)

    def save_dataframe(self):
        csv_name = self.name + '.csv'
        save_path = self.labor_csv_path + csv_name
        df.to_csv(save_path)











def get_start_data_from_calendar_week(year, calendar_week):
    '''Solution from Ron on stackoverflow
       https://stackoverflow.com/questions/51194745/get-first-and-last-day-of-given-week-number-in-python
    '''
    monday = datetime.datetime.strptime(f'{year}--{calendar_week}--1', "%Y-%W-%w").date()
    return monday

def get_week_number_from_isodate(year, month, day):
    wk_number = datetime.date(year, month, day).isocalendar()[1]
    return wk_number

if __name__ == '__main__':
   #parser = argparse.