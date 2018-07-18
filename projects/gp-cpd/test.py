import numpy as np 
from matplotlib import pyplot as plt 

N = 100
X = np.linspace(0.,1.,N) # [0,1] 사이에 균일한 거리를 둔 500 개의 point 정의
X = X.reshape((-1,1)) # reshape X to make it n*1