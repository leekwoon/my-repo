import numpy as np
from copy import copy

def get_data(name):
    """Generate data.

    This function is temporarily implemented. It will be modified soon.

    Arguments:
        name: The name of data.
        
    Returns:
        pair of x, y, f
    """
    if name == "Parabola":
        def func1(x):
            return x**2 - 0.5

        def func2(x):
            return 0.5 * x ** 2

        change_id = np.array([0 , round(np.random.uniform(75, 125)), round(np.random.uniform(175, 225))])
        change_id = np.array([0, 100, 200])
        cluster_id = np.array([0, 1, 0])
        cluster = [func1, func2]

        x_temp = np.random.uniform(size=400) * 2 - 1
        y1 = x_temp**2 - 0.5
        y2 = 0.5 * x_temp ** 2 

        x = np.zeros(400)
        y = np.zeros(400)
        wn = 0.15

        for i in range(400):
            rr = np.random.randint(0, 400)
            x[i] = x_temp[rr]  
            curr_num = cluster_id[max(np.where(i >= change_id)[0])]
            y[i] = cluster[curr_num](x_temp[rr])

        f = copy(y)
        y = y + np.random.normal(size=len(y)) * wn

        return x, y, f
    else:
        raise NotImplementedError("")
