"""
Problem 31 - Coin Sums
-------------------------------------------------------------------------------
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
# Coin sums
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# How many different ways can £2 be made using any number of coins?
coins = [1, 2, 5, 10, 20, 50, 100, 200]
DESIRED_SUM = 200

path_count = 0


def createCoinSolution(current_path, coins_left, current_sum):
    global path_count
    next_path = None

    # A solution is found
    if current_sum == DESIRED_SUM:
        path_count += 1
        return current_path

    # Coins must be removed after their usefulness is exhausted to avoid repeats, such as :
    # 1+2 != 2+1; Which is not desired so all coins can only be consecutively
    if current_sum < DESIRED_SUM:
        next_coins_left = coins_left[:]
        for coin in coins_left:
            next_path = current_path + str(coin)
            next_sum = current_sum + coin

            coin_solution = createCoinSolution(next_path, next_coins_left, next_sum)

            next_coins_left.remove(coin)
    return None


createCoinSolution("", coins, 0)
print(f'Path Count: {path_count}')
