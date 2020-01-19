import ftx
import liquidity_monitor

import pprint


pp = pprint.PrettyPrinter(indent=4)

print("Press 1 to see current liquidity")


user_choice = int(input())

if user_choice == 1:

    print("Sending API call - please wait approx 20 seconds")

    liquidity = liquidity_monitor.get_liquidity(0.2)

    pp.pprint(liquidity)
    