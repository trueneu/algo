import sys
stock_prices_yesterday = [10]


def get_max_profit(stocks):
    if len(stocks) < 2:
        raise Exception("There must be at least two prices")
    min_price_so_far = stocks[0]
    curr_profit = -sys.maxsize
    i = 1
    while i < len(stocks):
        price = stocks[i]
        curr_profit = max(curr_profit, price - min_price_so_far)
        min_price_so_far = min(min_price_so_far, price)
        i += 1
    return curr_profit

print(get_max_profit(stock_prices_yesterday))
