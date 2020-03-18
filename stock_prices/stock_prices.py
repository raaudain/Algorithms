#!/usr/bin/python

# Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

# ## Hints

#  For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

#  So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 


import argparse

def find_max_profit(prices):
  #pass
  # paid = 0
  # sold = 0
  
  # profit = sold - paid
  
  # def paid_price(prices):
  #   for i in range(0, len(prices)-1):
  #     current_min_price_so_far = i
  #     lowest_price = current_min_price_so_far
      
  #     for j in range(current_min_price_so_far+1, len(prices)):
  #       if prices[j] < prices[lowest_price]:
  #         lowest_price = j
          
  #     if current_min_price_so_far != lowest_price:
  #       temp = prices[lowest_price]
  #       prices[lowest_price] = prices[current_min_price_so_far]
  #       prices[current_min_price_so_far]: temp
  #     else:
  #       paid = prices[current_min_price_so_far]
    
  #   return paid_price
  
  # def sold_price(prices):
  #   for i in range(0, len(prices)-1):
  #     current_max_price_so_far = i
  #     highest_price = current_max_price_so_far

  #     for j in range(current_max_price_so_far+1, len(prices)):
  #       if prices[j] > prices[highest_price]:
  #         highest_price = j
          
  #     if current_max_price_so_far != highest_price:
  #       temp = prices[highest_price]
  #       prices[highest_price] = prices[current_max_price_so_far]
  #       prices[current_max_price_so_far]: temp
  #     else:
  #       sold = prices[current_max_price_so_far]
  
  #   return sold_price
  
  
  
  return find_max_profit(profit)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  
  
#print(find_max_profit([10, 7, 5, 8, 11, 9]), 6)