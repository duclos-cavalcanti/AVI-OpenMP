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

def async_value_iteration(value_arr:np.array, policy_arr:np.array, values:np.array, indices:np.array, indptr:np.array, shape:np.array, n_stars:int, nr_states:int, nr_actions:int) -> (np.array, np.array):
    """
    C++ version backend

    """
    _ffi = FFI()

    value_arr_ptr = _ffi.cast("float*", value_arr.ctypes.data)
    policy_arr_ptr = _ffi.cast("int*", policy_arr.ctypes.data)
    values_ptr = _ffi.cast("float*", values.ctypes.data)
    indices_ptr = _ffi.cast("int*", indices.ctypes.data)
    indptr_ptr = _ffi.cast("int*", indptr.ctypes.data)

    rows, cols = shape
    nr_nonzero = values.__len__()

    cpp_interface.lib.async_value_iteration(value_arr_ptr, policy_arr_ptr, values_ptr, indices_ptr, indptr_ptr, nr_nonzero, cols, rows, n_stars, nr_states, nr_actions)

    return value_arr, policy_arr
