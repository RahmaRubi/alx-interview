def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    
    Args:
    coins (list): List of coin denominations.
    total (int): Total amount to achieve with the coins.
    
    Returns:
    int: Fewest number of coins needed, or -1 if impossible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many of the current coin as possible
        count += total // coin
        total %= coin

    # If the total is not met, return -1
    return count if total == 0 else -1
