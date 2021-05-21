
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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
    states_sorted = states_df.sort_values(['cases_avg_per_100k']).reset_index()
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
    fig = plt.figure()
    for state in states_to_plot:
            state_cases_df = df[df.state == state]
            plt.plot(pd.to_datetime(state_cases_df.date),state_cases_df.cases_avg_per_100k, label = state)
            plt.xlabel('Date')
            plt.ylabel('Average Cases per 100k')
            plt.title(f'Covid Cases in {states_to_plot[0]}, {states_to_plot[1]}, and {states_to_plot[2]}')
            plt.legend()
            ax=plt.gca()
            fig.autofmt_xdate()
    return ax,states_to_plot

      
def modify_plot(ax,states_to_plot):
    '''
    This function modifies date formatting on plot to make them look better.
    INPUT: 
    ax: handle to current plot
 
    '''
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%y'))
    ax.tick_params(labelsize=7)
  
   
