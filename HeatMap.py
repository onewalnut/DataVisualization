#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : HeatMap
# @Author: HT
# @Date  : 2019/2/20
# @Desc  :

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
import numpy as np
x, y = np.random.rand(10), np.random.rand(10)
z = (np.linspace(0, 1, 9000000)).reshape(3000, 3000)
# z = np.array([[1,2],[1,3]])
plt.imshow(z+10, extent=(0, 1, 0, 2),
        cmap=cm.hot)
plt.colorbar()
plt.show()
