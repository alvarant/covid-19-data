
import pandas as pd
import matplotlib.pyplot as plt

def read_in_data(filename):
    '''
    INPUT: 
    filename: path to file name: e.g. /home/shared_data/covid-19-data/rolling-averages/us-states.csv
    OUTPUT: Pandas dataframe - converted from csv input
    '''
    df = pd.read_csv(filename)
    return df
    
def get_extreme_states(df, num_states):
     '''
    INPUT: 
    df: Pandas dataframe with raw state data
    num_states: The number of states to include on either extreme end (e.g. 5 will return 5 states with lowest and overall average covid
    cases per 100k)
    OUTPUT: 
    low_states: states with lowest covid cases
    high_states: states with highest covid cases
    '''
    states_df = df.groupby(by=['state']).agg({'cases_avg_per_100k':['sum']})
    states_df.columns=['cases_avg_per_100k']
    states_sorted = states_df.sort_values(['cases_avg_per_100k'])
    low_states = states_sorted.state.head(num_states).tolist()
    high_states = states_sorted.state.tail(num_states).tolist()
    return low_states,high_states    
          
def make_plot(df,states_to_plot):
     '''
    INPUT: 
    df: Pandas dataframe with raw state data
    states_to_plot: list of states to plot (e.g. ['Oregon','Texas','California'])
    OUTPUT: 
    ax: handle to current plot
    '''
    ...
        
    
   
      
def modify_plot(ax,states_to_plot):
     '''
    This function modifies date formatting on plot to make them look better.
    INPUT: 
    ax: handle to current plot
 
    '''
    
    ...
  
   
