import ftx
import markets
import liquidity_monitor
import scanner


import pprint


markets = markets.Markets()


pp = pprint.PrettyPrinter(indent=4)

print("Select option and press enter")
print(" ")
print("1: see current liquidity")
print("2: run market scan")




user_choice = int(input())

if user_choice == 1:

    print("Sending API call - please wait approx 20 seconds")

    liquidity = liquidity_monitor.get_liquidity(markets, 0.2)

    pp.pprint(liquidity)
    
elif user_choice == 2:

    print("Sending API call - please wait approx 20 seconds")

    scan_results = scanner.run_scan()

    pp.pprint(scan_results)