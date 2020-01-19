
print("")
print("Please wait, importing data from FTX API")


import ftx
import markets
import liquidity_monitor
import scanner
import analyser


from johansen import coint_johansen


import pprint




markets = markets.Markets()
scanner = scanner.Scanner()



pp = pprint.PrettyPrinter(indent=4)

print("Select option and press enter")
print(" ")
print("1: see current liquidity")
print("2: run market scan")
print("3: Run Johansen test on pair")




user_choice = int(input())

if user_choice == 1:

    print("Please enter tolerable slippage %")
    print("For example 0.2 for 0.2 %")


    tolerable_slippage = float(input())

    

    print("Sending API call - please wait approx 20 seconds")



    liquidity = markets.get_liquidity(tolerable_slippage)

    pp.pprint(liquidity)
    
elif user_choice == 2:

    print("Sending API call - please wait approx 20 seconds")

    scan_results = scanner.run_pairs_scan()

    pp.pprint(scan_results)

elif user_choice == 3:

    print("Please enter the first ticker e.g LTC-PERP")

    ticker_1 = str(input())
    
    print("Please enter the second ticker e.g DOGE-PERP")

    ticker_2 = str(input())

    analyser = analyser.Analyser(ticker_1, ticker_2)
    results = analyser.show_scores()

    print(" ")
    print("Trace Statistics")
    print(f"VS: {results[0]}")
    print(f"Crit-90%: {results[1]}")
    print(f"Crit-95%: {results[2]}")
    print(f"Crit-99%: {results[3]}")
    print(f"EV: {results[4]}")
    print(f"Crit-90%: {results[5]}")
    print(f"Crit-95%: {results[6]}")
    print(f"Crit-99%: {results[7]}")

