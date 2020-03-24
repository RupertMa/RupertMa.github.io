from scipy.stats import norm
from math import sqrt
import sys

       

def get_z_score(alpha):
    return -norm.ppf(alpha/2)

def get_beta(z_score, s, d_min, N):
    SE = s / sqrt(N)
    return norm.cdf(z_score * SE, loc=d_min, scale=SE)


def calculate_required_size(s, d_min, Ns=20000, alpha=0.05, beta=0.2):
    """
     :param s: The standard error of the metric with N=1 in each group
     :param d_min: The practical significance level
     :param Ns: The sample sizes to try
     :param alpha:  The desired alpha level of the test
     :param beta: The desired beta level of the test
     :return: The smallest N out of the given Ns that will achieve the desired
              beta. There should be at least N samples in each group of the experiment.
              If none of the given Ns will work, returns -1. N is the number of
              samples in each group.
    """          
    if get_beta(get_z_score(alpha), s, d_min, Ns) > beta:
        return -1
    left = 1
    right = Ns
    while left <= right:
        mid = (left + right) // 2
        ans = get_beta(get_z_score(alpha), s, d_min, mid)
        if ans <= beta:
            right = mid - 1
        elif ans > beta:
            left = mid+1
    return mid


if __name__=='__main__':
    s, d_min = float(sys.argv[1]), float(sys.argv[2])
    print(calculate_required_size(s, d_min))