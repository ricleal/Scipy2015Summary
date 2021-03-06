from mpi4py import MPI
import numpy as np

'''
MPI script called from IPython parallel client
'''
def psum(a):
    print 'Running MPI for',a
    locsum = np.sum(a)
    rcvBuf = np.array(0.0,'d')
    MPI.COMM_WORLD.Allreduce([locsum, MPI.DOUBLE],
        [rcvBuf, MPI.DOUBLE],
        op=MPI.SUM)
    return rcvBuf
