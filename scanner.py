# This notebook checks all possible pair combinations of perpetual swap contracts on FTX exchange
# and returns the charts of those that are below a certain percent of the moving average

# (not a trade signal on its own ?as not all the means are sufficiently stationary)

# The commented-out bits of code in cell 4 allow a different filter such as bollinger bands, or whether
# the difference between ratio and moving average is unusually high for that given pair

import ftx
import markets

import pandas as pd
import numpy as np

myClient = ftx.FtxClient()

markets = markets.Markets()



def sortSecond(val): 
    return val[1] 


def run_scan():
  
    # Get all the perps

    only_perps = markets.only_perps

    # Remove btc and usdt 
    only_perps.remove('BTC-PERP')
    only_perps.remove('USDT-PERP')

    # Get the data, and add it to a list with the data and the name of the data
    hist_prices_list = []
    [hist_prices_list.append([p, myClient.get_hist_futures(p, '3600')]) for p in only_perps]

    #[hist_prices_list.append([f, myClient.get_hist_futures(f, '3600')]) for f in futures_list]


    #Use the data to make a dataframe, and use the name to make a new column in the dataframe

    hist_dfs = []

    for hp in hist_prices_list:
        
        future_name = hp[0]
        future_data = hp[1]
        df = pd.DataFrame(future_data)
        df['future_name'] = future_name
        
        hist_dfs.append(df)
        

    # Put them into an array with the name of the ratio pair, and then the df of it

    coint_dfs = []

    for df in hist_dfs:
        
        
        x_df = df
        x_name = x_df['future_name'][0]
        
        for df in hist_dfs:
            
            y_name = df['future_name'][0]
            
            new_df = x_df.merge(df, on='startTime', how='inner')
            
            

            new_df = new_df[['close_x', 'close_y']]
            
            
            name = f'{x_name}/{y_name}'
            
            row = [name, new_df]
            
            coint_dfs.append(row)

            

            
            
            
        
            
    diverged_pairs = []

    for row in coint_dfs:
        
        
        row[1]['ratio'] = row[1].close_x / row[1].close_y
        row[1]['sma'] = row[1].ratio.rolling(75).mean()
        
        dist_pct = ( abs(row[1]['ratio']  - row[1]['sma']) / row[1]['sma'] ) * 100
        
        max_dist = dist_pct[-500:-10].max()
        
        pct = ((row[1].ratio.iloc[-1] - row[1].sma.iloc[-1]) / row[1].sma.iloc[-1] )  * 100
        
    
        
        if pct > max_dist * 0.8:
            

            diverged_pairs.append([row[0], pct])
            
            diverged_pairs.sort(key=sortSecond, reverse=True)

            return diverged_pairs
