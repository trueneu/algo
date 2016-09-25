global_denominations = [1, 5, 10]
global_money = 10


def cashier(denominations, money):
    memo = [[0 for _ in range(len(denominations))] for _ in range(money + 1)]

    for j in range(len(memo[0])):
        memo[0][j] = 0

    for i in range(1, money + 1):
        for j in range(len(memo[i])):
            ways_pure = 1 if i == denominations[j] else 0

            ways_addition = memo[i][j - 1]
            money_remainder = i - denominations[j]

            if money_remainder > 0:
                ways_addition2 = memo[money_remainder][j]
            else:
                ways_addition2 = 0

            ways_total = ways_pure + ways_addition + ways_addition2
            memo[i][j] = ways_total

    return memo[-1][-1]


print(cashier(global_denominations, global_money))