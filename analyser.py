import ftx
import settings
from johansen import coint_johansen

import pandas as pd
import numpy as np


client = ftx.FtxClient()



class Analyser:

    def __init__(self, ticker_1, ticker_2):

        data_1 = client.get_hist_futures(ticker_1, settings.candle_size)
        data_2 = client.get_hist_futures(ticker_2, settings.candle_size)

        df_1 = pd.DataFrame(data_1)
        df_2 = pd.DataFrame(data_2)

        merged_df = df_1.merge(df_2, on='startTime', how='inner')

        self.merged_df = merged_df[['close_x', 'close_y']]


    def run_coint_test(self):

        result = coint_johansen(self.merged_df, 0 , 1) 

        return result

    def check_result(self, result):
    
        vs = result.lr1[0]
        
        vs_pct_90 = result.cvt[0][0],
        vs_pct_95 = result.cvt[0][1],
        vs_pct_99 = result.cvt[0][2],
        
        ev = result.lr2[0],
        ev_pct_90 = result.cvm[0][0],
        ev_pct_95 = result.cvm[0][1],
        ev_pct_99 = result.cvm[0][2]

        results_array = [vs, vs_pct_90, vs_pct_95, vs_pct_99, ev, ev_pct_90, ev_pct_95, ev_pct_99]
        
                
        return results_array

    def show_scores(self):

        result = self.run_coint_test()
        scores = self.check_result(result)
        return scores






