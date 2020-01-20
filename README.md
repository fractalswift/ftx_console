
Suite of mini modules for working with FTX if you want to look for pair trades. Simple command line interface.


1. You can quickly estimate maximum liquidity across markets based on your maxmum tolerable slippage, based on order books.

2. You can quickly scan the market for unusually diverged pairs based on settings you choose in settings.py

3. You can run the johansen test on any pairs of perpetual swap contracts

Uses Python 3.

    Dependences: statsmodels, pandas, numpy

Uses the Johansen Test adapted for Python by James P. LeSage, University of Toledo. Version in this repo is modified a little to work 
with the rest of the module, you can find the orignal code here: https://programtalk.com/vs2/python/1807/quant_at/book/johansen.py/

Uses the FTX client module by the FTX team with a couple of extra methods. 



To run:

Just clone this repository, make sure you have the right dependences, go the directory and run:
    
    python3 ftx_console.py 
    
    
Then just follow the instructions.

You can edit the settings for the scanner in settings.py


To understand the Johansen test results, you can learn about the test here:

https://en.wikipedia.org/wiki/Johansen_test


DOCKER --- 

Also available as a docker image here:

    docker pull fractalswift/ftx-console

then run:

    run -i -t  ftx-console

Please be aware of multiple comparisons bias!


Disclaimer: I accept no responsibility if you lose money trading on FTX or anywhere else!


    
    
