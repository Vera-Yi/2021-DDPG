import random
import numpy as np 

class OU(object):

    def function(self, x, mu, theta, sigma):
        return theta * (mu - x) + sigma * np.random.randn(1)
    #theta--how fast variable regress mean    mu--balance     sigma--fluctuation