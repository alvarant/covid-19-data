import pandas as pd
import matplotlib.pyplot as plt
import math
import matplotlib.dates as mdates

def read_in_data(filename):
    '''
    INPUT: 
    filename: path to file name: e.g. /home/shared_data/covid-19-data/rolling-averages/us-states.csv
    OUTPUT: Pandas dataframe - converted from csv input.
    '''
    covid_df = pd.read_csv(filename)
    return covid_df
    
def get_extreme_states(covid_df, num_states):

    '''
    INPUT: 
    df: Pandas dataframe with raw state data
    num_states: The number of states to include on either extreme end (e.g. 5 will return 5 states with lowest and overall average covid
    cases per 100k)
    OUTPUT: 
    low_states: states with lowest covid cases
    high_states: states with highest covid cases
    '''
    agg_df=covid_df[['state','cases_avg_per_100k']].groupby('state').agg('mean')
    sorted_df = agg_df.sort_values(by=['cases_avg_per_100k'])
    low_states=sorted_df.head(num_states)
    high_states=sorted_df.tail(num_states)
    return low_states,high_states
  
          
def make_plot(covid_df,states_to_plot):
    '''
    INPUT: 
    df: Pandas dataframe with raw state data
    states_to_plot: list of states to plot (e.g. ['Oregon','Texas','California'])
    OUTPUT: 
    ax: handle to current plot
    '''
   
    for high_state in states_to_plot:
        given_state_df = covid_df[covid_df.state == high_state]
        plt.plot(pd.to_datetime(given_state_df.date), given_state_df.cases_avg_per_100k, label = high_state)
    plt.xlabel('date')
    plt.ylabel('covid infections per 100k')
    plt.legend(loc='upper left')
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    return ax,high_state

def modify_plot(ax,states_to_plot):
    '''
    This function modifies date formatting on plot to make them look better.
    INPUT: 
    ax: handle to current plot
 
    '''
    ax.set_xlabel('date')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%y'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.tick_params(axis='x',labelsize=8,rotation=40)
    
   
   
