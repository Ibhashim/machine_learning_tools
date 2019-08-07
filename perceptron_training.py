# labels should be a list containing the results for each data combination e.g. labels = [1, 0, 1]
# data list should be a list containing all the data combinations as indivdiual lists e.g. data_list = [[1, 3, 4], [2, 0, 0], [1, 4, 6]]
# where the first list is the first feature, second list is second feature etc.

# threshold should be the value above which the perceptron should fire
# weights are preset to 0 (if random), user can modify if they have some preset knowledge
# increase or decrease learning_rate to change speed at which weights change

def perceptron_training(labels, data_list, threshold, weights = [0], learning_rate = 1.0): 
    generation_counter = 1
    predicted_ys = []
    
    if weights == [0]: # if user specified no weights, make weights list length needed
        for i in range(len(data_list[0]) - 1):
            weights.append(0)
    
    print(weights)
        
    for i in range(len(data_list)):
        data[i] = max_min_standardisation(data[i]) # bring all features to same scale using function in this project repository

    while predicted_ys != labels:
        i = 0
        predicted_ys = []
        
        while i != len(data):
            training_data = []
            for j in range(len(data[i])):
                training_data.append(data[j][i])

            label = labels[i]
            output = sum([w*x for w, x in zip(weights, training_data)]) # calculate output by multiplying weights with training_data

            if output >= threshold:
                predicted_ys.append(1)
            else:
                predicted_ys.append(0)

            if label == 1 and output < threshold: # if undercalculation
                weights = [w+(x*learning_rate) for w,x in zip(weights, training_data)] # increase ws
            elif label == 0 and output >= threshold: # if overcalculation
                weights = [w-(x*learning_rate) for w, x in zip(weights, training_data)] # decrease ws
            else:
                pass

            i += 1

        print('Generation ' + str(generation_counter))
        generation_counter += 1
        
    return(weights)
