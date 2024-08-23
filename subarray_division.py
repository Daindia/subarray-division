def subarray_division(chocolate_bar, birth_date, birth_month):
    
    ways_divide = 0
    first_index = 0
    last_index = birth_month
    for rotation in chocolate_bar:
        if sum(chocolate_bar[first_index:last_index]) == birth_date:
            ways_divide += 1
        first_index += 1
        last_index += 1
    
    return ways_divide