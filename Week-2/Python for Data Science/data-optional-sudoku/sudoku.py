# pylint: disable=missing-docstring

import numpy as np

def sudoku_validator(grid):
    grid_arr = np.array(grid)

    rows = all(all(x in grid_arr[num,:] for x in range(1,10)) for num in range(9))
    cols = all(all(x in grid_arr[:,num] for x in range(1,10)) for num in range(9))

    upper_left = all(x in grid_arr[:3,:3] for x in range(1,10))
    upper_mid = all(x in grid_arr[:3,3:6] for x in range(1,10))
    upper_right = all(x in grid_arr[:3,6:9] for x in range(1,10))

    mid_left = all(x in grid_arr[3:6,:3] for x in range(1,10))
    mid = all(x in grid_arr[3:6,3:6] for x in range(1,10))
    mid_right = all(x in grid_arr[3:6,6:9] for x in range(1,10))

    lower_left = all(x in grid_arr[6:9,:3] for x in range(1,10))
    lower_mid = all(x in grid_arr[6:9,3:6] for x in range(1,10))
    lower_right = all(x in grid_arr[6:9,6:9] for x in range(1,10))

    if all([rows,cols,upper_left,upper_mid,upper_right,mid_left,mid,mid_right,
            lower_left,lower_mid,lower_right]):
        return True
    return False
