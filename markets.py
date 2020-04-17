import ftx
import pandas as pd
import numpy as np


myClient = ftx.FtxClient()


class Markets:

    def __init__(self):

        # Get all the perps

        self.futures = pd.DataFrame(myClient.list_futures())
        self.markets = pd.DataFrame(myClient.list_markets())
        self.futures_list = self.futures.name.tolist()

        # Just get the perps for now:

        self.only_perps = []

        [self.only_perps.append(f) for f in self.futures_list if 'PERP' in f]

    def get_liquidity(self, tolerable_slippage):

        # Get the liquidity

        tickers = self.only_perps

        pct = tolerable_slippage  # tolerable slippage %

        pct = pct / 100

        info = []

        for ticker in tickers:

            t = myClient.get_orderbook(ticker)
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
