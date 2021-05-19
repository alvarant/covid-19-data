import pandas as pd
import matplotlib.pyplot as plt

def read_in_data(filename):
    '''
    INPUT: 
    filename: path to file name: e.g. /home/shared_data/covid-19-data/rolling-averages/us-states.csv
    OUTPUT: Pandas dataframe - converted from csv input.
    '''
    covid_df = pd.read_csv('/home/shared_data/covid-19-data/rolling-averages/us-states.csv')
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
    agg_df=covid_df[['cases_avg_per_100k', 'state']].groupby('state').agg('mean')
    low_states=agg_df.head(3)
    high_states=agg_df.tail(3)
    return low_states,high_states
  
          
def make_plot(covid_df,states_to_plot):
     '''
    INPUT: 
    df: Pandas dataframe with raw state data
    states_to_plot: list of states to plot (e.g. ['Oregon','Texas','California'])
    OUTPUT: 
    ax: handle to current plot
    '''
   
    for state in states_to_plot:
        given_state_df = covid_df[covid_df.state == state]
        plt.plot(pd.to_datetime(given_state_df.date), given_state_df.cases_avg_per_100k, label = state)
        
        
    
 
      
def modify_plot(ax,states_to_plot):
     '''
    This function modifies date formatting on plot to make them look better.
    INPUT: 
    ax: handle to current plot
 
    '''
    
   
   
