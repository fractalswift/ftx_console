import pandas as pd
import numpy as np
import ftx
import markets


markets = markets.Markets()
client = ftx.FtxClient()



def get_liquidity(markets, tolerable_slippage):
   
   # Get the liquidity

    tickers = markets.only_perps

    pct = tolerable_slippage # tolerable slippage %

    pct = pct / 100

    info = []

    for ticker in tickers:
        
        t = client.get_orderbook(ticker)
        best_price = t.get('asks')[0][0]
        
        worst_price = best_price * (1 + pct)
        
        totals = []
        
        for a in t.get('asks'):
            
            if a[0] < worst_price:
                
                total = a[0] * a[1]
                totals.append(total)
            
        row = [ticker, sum(totals)]
        
        info.append(row)
        
        
    # Sort info by lowest liquidity first

    info.sort(key=lambda x: x[1])

    return info
            
            

        
        
        