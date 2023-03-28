import numpy as np
vac_nums = [0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3
            ]
a = np.array(vac_nums)
mean = np.sum(a)/a.size
v =np.sum((a-mean)**2)/a.size
print(v)