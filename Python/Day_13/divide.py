def divide(dividend, divisior):
    if not divisior:
        return None
    quotient = dividend
    remainder = dividend % divisior
    return quotient, remainder

q, r = divide(35, 4)
