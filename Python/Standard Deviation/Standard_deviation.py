def std_dev(X):
    """
    Compute the standard deviation
    
    Argument:
        X: list of integers
    Return:
        sigma: float
    """
    return (sum((X[i] - (sum(X)/len(X)))**2 for i in range(len(X)))/(len(X)-1))**0.5
    
    
X = [float(x) for x in input().split(',')]
sigma = std_dev(X)
print(f'{sigma:.2f}')
