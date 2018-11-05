import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="Total number to be chosen from")
parser.add_argument("-k", type=int, default=0, help="Number of ways to choose from n")
parser.add_argument("--test",action="store_true", help="Runs the test module")
parser.add_argument("--log",action="store_true", help="Return the log of the binomial coeficient. if not used, will return the binomial coeficient")
args = parser.parse_args()
 
    
def logfactorial(n,k=0):
    '''Function to calculate the log of n!, by summing the log(1)...log(n). This calculates log(n!/k!).
    Examples:
    >>> logfactorial(5,3)
    2.995732273553991
    >>> logfactorial(5,5)
    0
    >>> logfactorial(5,6)
    0
    '''
    assert n>=0, 'n should be a positive values'
    assert type(n) == int, 'n should be an integers'
    assert k>=0, 'k should be positive'
    output=0
 ### getting the logs of range(k+1, n+1) is equivalent to calculate log(n!/k!), because this is the same as summing the log of k+1, K+2,... until n. Ex: If n=4 and k=2, then log(n!/k!)=log 3 + log 4 ###
    for value in range(k+1,n+1):
        output += math.log(value)  
    return output


def choose(n=args.n, k=args.k, log=args.log):
    '''
    Function that outputs the number of times you can choose k values out of n.
    >>> choose(5,1)
    binomial coeficient:  5
    >>> choose(0,0)
    binomial coeficient:  1
    >>> choose(5,5)
    binomial coeficient:  1
    '''
    assert k<=n, 'k should be <=n'
    assert n>=0, 'n should be >=0'
# choose(n,k) = n!/(k! (n-k)!), which is equivalente in the log form to log(choose(n,k)) = log(n!/k!) - log((n-k)!). I am using the fuction logfactorial() to calculate a=log(n!/k!) and b=log((n-k)!).
    a = logfactorial(n,k)
    difference = n-k
    b = logfactorial(difference)
    output_choose=a-b
    if log:
        print ("log binomial coeficient: ", output_choose)
    else:
    #For this output, I rounded the number to get the real integer that represents the number of ways you can choose k from n. I am also usig the .exp function to get the coefficient without the log.  
        print("binomial coeficient: ", round(math.exp(output_choose)))
       
if __name__ == '__main__':
    if args.test:
        import doctest
        doctest.testmod()
choose()