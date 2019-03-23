import pandas as pd
import numpy as np
import datetime

import os
import argparse



class Labor(object):
    '''Class containing information needed to build a labor profile'''

    def __init__(self, name, 
                 labor_df=None,
                 contract='contract_00',
                 projects, hourly_rate=100,
                 labor_csv_path="~/generic_path/"):
        # name (str): name of employee
        # contract (str): contract name employee is working under
        # projects (list): list of project names employee is working
        # labor_csv_path (str): path of labor csv file
        self.name = name
        self.contract = contract
        self.projects = projects
        self.hourly_rate = hourly_rate
        self.labor_csv_path = labor_csv_path
        if labor_df:
            self.labor_df = labor_df
        else:
            for _,_,files in os.walk(self.labor_csv_path):
                if name + '.csv' in files:
                    labor_df = self.load_dataframe(labor_csv_path + name + '.csv')
                else:
                    labor_df = generate_labor_df()

    def generate_empty_labor_df(self):
        project_hours = dict()
        wk_numbers = range(52)
        current_year = datetime.datetime.now().year
        columns = []
        for wk_number in wk_numbers:
            monday = get_start_data_from_calendar_week(current_year, wk_number)
            columns.append(monday)

        rows = []
        for project in projects:
            projected = project + '_estimated'
            actuals = project + '_actuals'
            rows.append(projected)
            rows.append(actuals)

        labor_df = pd.DataFrame(0, index=rows, columns=columns)

    def insert_project_hours(self, project, hours, 
                   date=datetime.datetime.now(), estimated=True):
        year = date.year
        month = date.month
        day = date.day
        wk_number =  get_week_number_from_isodate(year, month, day)
        monday = get_start_data_from_calendar_week(year, wk_number)
        if estimated:
            row = project + '_estimated'
        else:
            row = project + '_actuals'
        labor_df.iloc[row, monday] = hours
        return

    def map_actual_to_estimated_hours(self, project):
        estimated = labor_df[project +'_estimated']
        actuals = labor_df[project + '_actuals']
        dates = labor_df.index.values.tolist()

    def load_dataframe(self, load_path):
       return pd.read_csv(load_path)

    def save_dataframe(self):
        csv_name = self.name + '.csv'
        save_path = self.labor_csv_path + csv_name
        df.to_csv(save_path)



# Create labor objects and dataframes from larger excel sheet
def load_labor_from_excel(excel_path, *args, **kwargs):
    opt_path = os.path.normpath(excel_path)
    df = pd.read_excel(os_path)
    # Fill NaNs in column names with name of corresponding employee
    df.column = pd.Series(df.column).fillna(method='ffill')
    # do the same with months in indices
    df.index = pd.Series(df.index).fillna(method='ffill')
    # convert week numbers in first column to date of first monday
    # in corresponding week



def create_labor_excelsheet(list_of_labor, excel_path, *args, **kwargs):
    '''Creates an excel spreadsheet from labor objects initialized
       through this script
    '''
    for labor in list_of_labor:








def get_start_data_from_calendar_week(year, calendar_week):
    '''Solution from Ron on stackoverflow
       https://stackoverflow.com/questions/51194745/get-first-and-last-day-of-given-week-number-in-python
    '''
    monday = datetime.datetime.strptime(f'{year}--{calendar_week}--1', "%Y-%W-%w").date()
    return monday

def get_week_number_from_isodate(year, month, day):
    wk_number = datetime.date(year, month, day).isocalendar()[1]
    return wk_number

def load_dataframes_from_xlsx(xlsx, name=None, create_labor=False):
    '''loads labor dataframes from central excel file'''
    xlsx_file = pd.ExcelFile(xlsx)
    labor_dfs = {name: xlsx.parse(name) for name in xlsx.sheet_names}
    if name and create_labor:
        labor = Labor(name, labor_df=labor_dfs[name]) 
        return labor

        
    for name, df in labor_dfs.items()
        

if __name__ == '__main__':
   #parser = argparse.
