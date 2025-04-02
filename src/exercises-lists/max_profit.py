# =============================================================================
# Functions
# =============================================================================

def max_profit(prices: list[int]) -> int:
    """Calculates the maximum profit from buying and selling stock once.

    Given a list of stock prices where each price corresponds to a day in sequential time,
    this function determines the maximum profit that can be achieved by buying on one day 
    and selling on a later day.

    Args:
        prices (list[int]): List of stock prices.

    Returns:
        int: Maximum possible profit. Returns 0 if no profit is possible.
    """
    if len(prices) < 2:
        return 0
        
    max_profit = 0
    min_price = prices[0]

    for price in prices:
        curr_profit = price - min_price
        if curr_profit > max_profit:
            max_profit = curr_profit
        if price < min_price:
            min_price = price
    
    return max_profit