import ftx
import markets
import liquidity_monitor
import scanner


import pprint


markets = markets.Markets()
scanner = scanner.Scanner()


pp = pprint.PrettyPrinter(indent=4)

print("Select option and press enter")
print(" ")
print("1: see current liquidity")
print("2: run market scan")




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