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


