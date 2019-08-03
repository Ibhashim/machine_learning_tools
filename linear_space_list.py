def linear_space_list(min_value, max_value, number, decimal = 8):
    return [round(min_value + num*((max_value-min_value)/(number-1)), decimal) for num in range(0,number)]
