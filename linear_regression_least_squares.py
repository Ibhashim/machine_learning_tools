# Import libraries
import linear_space_list # part of this project repository
import matplotlib.pyplot as plt # library for visualisation

def linear_regression_least_squares(x_points, y_points):
    sum_x          = sum(x_points) # sum of all x points
    sum_x_squared  = sum([x**2 for x in x_points]) # sum of all x points squared
    sum_x_y        = sum([x*y for x, y in zip(x_points, y_points)]) # sum of all x * y points
    sum_y          = sum(y_points) # sum of all y points
    
    denominator    = (len(x_points) * sum_x_squared) - (sum_x*sum_x)
    slope          = ((len(x_points) * sum_x_y) - (sum_x * sum_y))/denominator # calculating slope
    intercept      = ((sum_x_squared * sum_y) - (sum_x * sum_x_y))/denominator # calculates intercept
    
    x_min = min(x_points)
    x_max = max(x_points)
    artifical_x    = linear_space_list(x_min, x_max, 10) # works same way as numpy.linspace(x_min, x_max, 10)
    predicted_y    = [m*x + c for x in artifical_x] 
    
    plt.scatter(x_points, y_points) # plots original data
    plt.plot(artifical_x, predicted_y) # plots least squares line
    
    return slope, intercept
