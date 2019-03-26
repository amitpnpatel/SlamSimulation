import numpy as np
import math


MAX_RANGE = 10
METRE_2_PIX = 100
MULTIPLIER = 2
DELTA_R = 0.01*MULTIPLIER
DELTA_THETA = 0.1*MULTIPLIER

cos = lambda x: np.cos(np.deg2rad(x))
sin = lambda x: np.sin(np.deg2rad(x))

len2ind = lambda cPos, rad, func, alpha: math.floor( (cPos + rad * func(alpha)) * METRE_2_PIX )
len2ind_np = lambda cPos, rad, func, alpha: np.floor( (cPos + rad * func(alpha)) * METRE_2_PIX )

def cart2pol(arr, current):
    xx = arr - current
    rho = np.sqrt(np.sum((xx) ** 2, axis=1))
    theta = np.rad2deg(np.arctan2(xx[:,1], xx[:, 0]))
    theta[np.sign(theta) == -1] += 360
    return np.column_stack((rho, theta))
