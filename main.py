def maxProfit(prices):
    cache = 0
    result = [None, 0]
    for price in prices:
        if result[0] == None:
            result[0] = price
        else:
            if result[0] < price and result[1] < price:
                result[1] = price
                value = result[1] - result[0]
                cache = max(cache, value)
            elif price < result[0]:
                result = [price, 0]
    return cache

prices = [7,1,5,3,6,4]

print(maxProfit(prices))