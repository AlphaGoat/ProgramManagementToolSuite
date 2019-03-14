import matplotlib.pyplot as plt
import numpy as np

import datetime

class Project(object):

    '''Class containing all relevant information about a project
       being worked on. Allows mapping of burn rates, schedule
       projections, dynamic assignment and reassignment of employees 
       to adjust burn rates to schedule requirements, and more
    '''

    def __init__(self, project_name, funds, allowed_carry_over,
            employees, init_date, end_date, *args, **kwargs):
        # Parameters:
        #       project_name (str): self-explanatory
        #       funds (float32): number giving the amount of money 
        #                        allocated to the project
        #       carry_over (float32): funds allowed to be carried 
        #                             to the next year
        #       init_date (str):  
        #       employees (list): list of 'employee' type objects
        self.__name__ = project_name
        self.funds = funds
        self.allowed_carry_over 
        self.employees = employees
        self.


    def map_burn(date):




    def flat_burn(funds, start_date, end_date):
        '''function that maps a flat burn rate over the weeks 
           remaining in the project
        '''






