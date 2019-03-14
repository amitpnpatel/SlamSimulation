import math
import numpy as np



MAX_RANGE = 10
METRE_2_PIX = 5
DELTA_R = 0.1
DELTA_THETA = 0.5

cos = lambda x: np.cos(np.deg2rad(x))
sin = lambda x: np.sin(np.deg2rad(x))

len2ind = lambda cPos, rad, func, alpha: math.floor( (cPos + rad * func(alpha)) * METRE_2_PIX )
