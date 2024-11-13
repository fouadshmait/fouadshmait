def  max_profit(prices):
  max_price=0
  min_price = float('inf')
  buy_price=0
  sell_price=0
  max_profit=0


  if len(prices) < 2:
    return 0
  for i in range (len(prices)):
     if min_price >prices[i]:
          min_price = prices[i]

     profit = prices[i] - min_price
     if max_price < prices[i]:
         max_price = prices[i]
     if max_profit < profit:
      max_profit = profit

  return max_profit


prices = [7,1,5,2] 
print(max_profit(prices))


