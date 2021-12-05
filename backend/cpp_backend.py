import numpy as np
import os, logging
from cffi import FFI

try:
  import cpp_interface

except (ModuleNotFoundError, ImportError) as e:
  print(f"Importing of Backend failed:\n{e}\n")
  raise

#########################
# Wrappers for c++ code #
#########################

def async_value_iteration(V:np.array, PI:np.array, values:np.array, indices:np.array, indptr:np.array, shape:np.array, n_stars:int, nS:int, nA:int) -> (np.array, np.array):
    """
    C++ version backend

    """
    _ffi = FFI()

    V_ptr = _ffi.cast("float*", V.ctypes.data)
    PI_ptr = _ffi.cast("int*", PI.ctypes.data)
    values_ptr = _ffi.cast("float*", values.ctypes.data)
    indices_ptr = _ffi.cast("int*", indices.ctypes.data)
    indptr_ptr = _ffi.cast("int*", indptr.ctypes.data)

    rows, cols = shape
    nnz = values.__len__()

    cpp_interface.lib.async_value_iteration(V_ptr, PI_ptr, values_ptr, indices_ptr, indptr_ptr, nnz, cols, rows, n_stars, nS, nA)

    return V, PI
