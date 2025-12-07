def format_won(amount):
    """
    Quick KRW formatter: rounds to nearest won and adds thousand separators.
    Example: 123456.87 -> "₩123,457"
    """
    try:
        amt = int(round(float(amount)))
    except Exception:
        amt = 0
    return f"₩{amt:,}"

def format_won_ticks(x, pos):
    """
    Formatter for matplotlib ticks: receives float x, returns '₩1,234' style string.
    """
    try:
        return f"₩{int(round(x)):,}"
    except Exception:
        return f"₩{x}"