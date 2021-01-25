#this is a very basic intro to parallel working
# here i will do different works in parallel

from joblib import Parallel, delayed
from math import sqrt


result = Parallel(n_jobs=2)(delayed(sqrt)(i ** 2) for i in range(10))

print(result)