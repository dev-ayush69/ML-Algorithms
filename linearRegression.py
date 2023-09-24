import numpy as np

def function(X,Y):
    x_mean = np.mean(X)
    y_mean = np.mean(Y)
    n = len(X)
    numerator = denominator = 0

    for i in range(n):
        numerator += (X[i] - x_mean) * (Y[i] - y_mean)
        denominator += (X[i] - x_mean) * (X[i] - x_mean)
        
    m = numerator/denominator
    c = y_mean - m * x_mean

    print("Slope of the line: ", m)
    print("Intercept: ", c)

if __name__ == "__main__":
    X = [1,2,3,4,5]
    Y = [4,7,10,13,16]

    function(X,Y)
