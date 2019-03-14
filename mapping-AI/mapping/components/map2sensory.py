# import numpy as np
# import math
# from mapping.components.constants import Action, Directions, MAX_RANGE, len2ind, cos, sin, DELTA_R, METRE_2_PIX, DELTA_THETA

# def sensor_array(current, direction, actual_map, fov):
#     #create sensory_array
#     xc, yc = current
#     x, y = direction

#     directionAngle = np.rad2deg(math.atan2(y, x))
#     if np.sign(directionAngle) == -1:
#         directionAngle += 360

#     size_sensory_array = int(fov//DELTA_THETA)
#     sensory_array = [np.inf for i in range(size_sensory_array)] #  np.ones(size_sensory_array, dtype=np.int) * np.inf


#     current_angle = directionAngle - ((size_sensory_array/2) * DELTA_THETA)

#     for scan in range(size_sensory_array):
#         for i in np.arange(0, MAX_RANGE, DELTA_R):

#             xInd, yInd = len2ind(xc, i, cos, current_angle), len2ind(yc, i, sin, current_angle)
#             if xInd in (-1, size_sensory_array) or yInd in (-1, size_sensory_array):
#                     sensory_array[scan] = np.sqrt((xInd/METRE_2_PIX)**2 + (yInd/METRE_2_PIX)**2)
#             else:
#                 val = actual_map[xInd, yInd]
#                 if val == 1:
#                     sensory_array[scan] = np.sqrt((xInd/METRE_2_PIX)**2 + (yInd/METRE_2_PIX)**2)

#         current_angle += DELTA_THETA

#     return sensory_array
