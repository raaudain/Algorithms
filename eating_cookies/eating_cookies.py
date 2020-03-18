#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  way = [1]
  ways = sum(way)
  
  if n <= 1:
    way.append(1)
  
  prev = eating_cookies(n-1)
  way.append(n * prev)
  
  return eating_cookies(ways)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
    
  print(eating_cookies(0))