def get_total_sum(baskets):
    total_sum = 0
    for basket in baskets:
        total_sum += basket.sum()
    return total_sum
