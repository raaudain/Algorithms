#!/usr/bin/python

# Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

# ## Hints

#  For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

#  So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 


import argparse

def find_max_profit(prices):
  
    # profits = []
    
    # for i in range(0, len(prices)-1):
    #   buy = i
    #   for j in range(i+1, len(prices)):
    #     current_sell = prices[j]
    #     current_buy = prices[buy]
    #     profit = current_sell - current_buy
    #     profits.append(profit)
    # return max(profits)
    #print(find_max_profit(stock_prices)
  
  # min_price = prices[0]
  # max_profit = prices[1] - min_price
  
  # for i in range(len(prices)):
  #   price = prices[i]
  #   max_profit = max(price - min_price, max_profit)
  #   min_price = min(price, min_price)
    
  # return max_profit
  
  profit = prices[1] - prices[0]
  
  # For i in prices array after index 1
  for i in prices[1:]:
    # If i minus the first element in prices is larger than profit
    if (i - prices[0]) > profit:
      # profit becomes i minus the first element in prices
      profit = i - prices[0]
    # If i is less that the first element in prices
    if i < prices[0]:
      # The first element of prices becomes i
      prices[0] = i
        
  return profit
 

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  
  
# print(find_max_profit([10, 7, 5, 8, 11, 9]), 6)