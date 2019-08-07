def max_min_standardisation(data): # takes list of data and standardises it between 0 and 1 then returns new list
    data_min = min(data)
    data_max = max(data)
    for i in range(len(data)):
        if data[i] == data_min:
            data[i] = 0
        elif data[i] == data_max:
            data[i] = 1
        else:
            data[i] = (data[i] - data_min)/(data_max - data_min)
    return(data)
