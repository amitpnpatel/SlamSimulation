import math
import numpy as np



MAX_RANGE = 10
METRE_2_PIX = 100
DELTA_R = 0.005
DELTA_THETA = 0.075

cos = lambda x: np.cos(np.deg2rad(x))
sin = lambda x: np.sin(np.deg2rad(x))

len2ind = lambda cPos, rad, func, alpha: math.floor( (cPos + rad * func(alpha)) * METRE_2_PIX )

def cart2pol(arr, current):
    xx = arr - current
    rho = np.sqrt(np.sum((xx) ** 2, axis=1))
    theta = np.rad2deg(np.arctan2(xx[:,1], xx[:, 0]))
    theta[np.sign(theta) == -1] += 360
    return np.column_stack((rho, theta))
