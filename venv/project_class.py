import matplotlib.pyplot as plt
import numpy as np

import datetime

class Project(object):

    '''Class containing all relevant information about a project
       being worked on. Allows mapping of burn rates, schedule
       projections, dynamic assignment and reassignment of employees 
       to adjust burn rates to schedule requirements, and more
    '''

    def __init__(self, project_name, contract, funds, 
            allowed_carry_over, milestones, employees, 
            init_date, end_date, *args, **kwargs):
        # Parameters:
        #       project_name (str): self-explanatory
        #       funds (float32): number giving the amount of money 
        #                        allocated to the project
        #       carry_over (float32): funds allowed to be carried 
        #                             to the next year
        #       init_date (str):  
        #       milestones (dict): dict with milestone names as
        #                          keys and  tuples containing percent
        #                          completion and dates in 'YYYY-mm-dd'
        #                          format as values
        #       employees (list): list of 'employee' type objects
        self.__name__ = project_name
        self.funds = funds
        self.allowed_carry_over 
        self.employees = employees
        # Get the current date
        now = datetime.datetime.now()
        self.current_date = now.strftime("%Y-%m-%d")
        self.args = args
            self.kwargs = kwargs

    def map_burn(date):
        pass

    def flat_burn(funds, start_date, end_date, funds_burned=0.0):
        '''function that maps a flat burn rate over the weeks 
           remaining in the project
        '''
        sd = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        ed = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        difference = ed - sd 
        wks_diff = difference.days/7
        funds_to_burn = funds - funds_burned
        burn_rate = funds_to_burn / wks_diff
        return burn_rate

    def get_burn_based_on_hours(
        





