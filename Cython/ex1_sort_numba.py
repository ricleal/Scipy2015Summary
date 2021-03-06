from numba import jit as numba_jit

@numba_jit
def numba_bubblesort(np_ary):
    """ The NumPy implementation of Bubblesort on NumPy arrays."""
    length = np_ary.shape[0]
    swapped = 1
    for i in xrange(0, length):
        if swapped:
            swapped = 0
            for ele in xrange(0, length-i-1):
                if np_ary[ele] > np_ary[ele + 1]:
                    temp = np_ary[ele + 1]
                    np_ary[ele + 1] = np_ary[ele]
                    np_ary[ele] = temp
                    swapped = 1
    return np_ary
