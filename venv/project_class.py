import matplotlib.pyplot as plt
import numpy as np

# Custom modules
import program_management_helpertools as pmh

import datetime

try:
    import cpickle as pickle
except ModuleNotFoundError:
    import pickle

class Project(object):

    '''Class containing all relevant information about a project
       being worked on. Allows mapping of burn rates, schedule
       projections, dynamic assignment and reassignment of employees 
       to adjust burn rates to schedule requirements, and more
    '''

    def __init__(self, project_name, contract, funds, 
            allowed_carry_over, milestones, employees, 
            init_date, end_date,
            project_dir = 'C:\Users\pthomas\Documents\MISS Documents\projects_dir',
            *args, **kwargs):
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
        self.end_date = end_date
        self.args = args
        self.kwargs = kwargs

    def map_burn(self, date):
        pass

    def flat_burn(self, funds=self.funds, start_date=self.start_date,
                  end_date=self.end_date, funds_burned=0.0):
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

    def get_burn_based_on_hours(self, start_date=self.start_date,
                                end_date=self.end_date, burn_type='flat',
                                save_plot=False):
        '''Check all hours employees have allocated against this project and
           calculate dollars burned up until the date specified'''
        start_datetime_object = pmh.convert_date_str_into_datetime_obj(date)
        end_datetime_object = pmh.convert_date_str_into_datetime_obj(date)
        prev_start_monday = datetime_object - timedelta(days=datetime_object)
        prev_end_monday = datetime_object - timedelta(days=datetime_object)
        num_wks = employees[0].labor_df.get_loc(prev_end_monday) - \
                        employees[0].labor_df.get_loc(prev_start_monday)
        total_projected_cost = np.ones(num_wks)
        total_actual_cost = np.ones(num_wks)
        for employee in employees:
            projected_hrs = employee.labor_df.loc[self.__name__ + '_estimated',
                                            prev_start_monday:prev_end_monday]
            actual_hrs =  employee.labor_df.loc[self.__name__ + '_actual',
                                            prev_start_mondat:prev_end_monday]
            employee_projected_cost = employee.hourly_rate * projected_hrs
            employee_actual_cost = employee.hourly_rate * actual_hrs
            total_projected_cost = total_projected_cost + employee_projected_cost
            total_actual_cost = total_actual_cost + employee_actual_cost

        # Get estimates for a burn
        if burn_type == 'flat':
            target_burn_rate = self.flat_burn()

        target_burn_array = np.ones(num_wks) * target_burn_rate

        # Plotting cost over dates
        dates = employees[0].labor_df.columns[prev_start_monday:prev_end_monday].values
        fig = plt.figure()
        ax1.add_subplot(111)
        ax1.plot(dates, total_projected_cost, label='projected_burn', color='b')
        ax1.plot(dates, total_actual_cost, label='actual_burn', color='r')
        ax1.plot(dates, flat_burn_array,label='targetted_burn', color='g')
        plt.xticks(dates)
        plt.xlabel('Date')
        plt.ylabel('Burn Rate ($)')
        if save_plot:
            plot_name = 'burnplot_' + end_date
            save_path = project_dir + self.__name__ + '\saved_lots' + plot_name
            plt.savefig(save_path)
        plt.show()
        return

    def save_project_object(self):
        return


        





