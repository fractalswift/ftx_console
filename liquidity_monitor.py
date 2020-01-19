import pandas as pd
import numpy as np
import ftx
client = ftx.FtxClient()

def get_liquidity(tolerable_slippage):
    # Get the list of perp tickers

    futures = pd.DataFrame(client.list_futures())
    futures_list = futures.name.tolist()
    only_perps = []
    [only_perps.append(f) for f in futures_list if 'PERP' in f]

    tickers = only_perps

    # Get the liquidity

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
            
            

        
        
        