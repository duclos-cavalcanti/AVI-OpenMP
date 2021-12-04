## C++ backend

import numpy as np ## array manipulations
import os, logging ## operating system operations, logging

_logger = logging.getLogger(__name__)

def _find_compile_output():
  """
  Returns all the files that belong to the compiled interface
  """
  def should_include(bar):
    """
    checks whether cpp_interface.cpp, cpp_interface.---.so and cpp_interface.o exist
    """
    return bar.startswith("cpp_interface") and bar.endswith((".cpp", ".o", ".so"))

  return [foo for foo in os.listdir(os.path.dirname(__file__)) if should_include(foo)]

def _compile_output_complete():
  """
  checks if exactly the desired 3 files exist
  """
  return len(_find_compile_output()) == 3

## if some compile issues occured
if not _compile_output_complete():
  from .compile_interface import compile_interface

  _logger.warning("Trying to compile the c++ backend now.")
  ## this is the folder in which backend_cpp.py is located
  current_dir = os.path.dirname(__file__)

  inc = os.path.join(current_dir, 'include')
  lib = os.path.join(current_dir, 'lib')

  if not os.path.exists(inc) or not os.path.exists(lib) or len(os.listdir(inc)) == 0 or len(os.listdir(lib)) == 0:
    raise ImportError("The include and/or library folder is not existing or empty, did you run 'make install'?")

  os.chdir(current_dir)
  compile_interface(verbose=True)
  os.chdir("..")

## if some errors issues occured
if not _compile_output_complete():
  _logger.error("The expected compilation output is incomplete, stopping here!")
  raise ImportError("The compilation of the c++ python interface was not successful.")

try:
  from . import cpp_interface
  from cffi import FFI

except (ModuleNotFoundError, ImportError) as e:
  _logger.error(f"Compiled interface is present, yet importing failed.\nReason:\n\n{e}\n\n")
  raise

## for casting the pointers
_ffi = FFI()

#############################
# Wrappers for the c++ code #
#############################

def example_func(i:int) -> (int):
  """
  C++ version backend
  """
  ## check dtypes of values, indptr and indices
  # if i.dtype != int:
  #   raise TypeError("Datatype missmatch for i")

  # i_ptr = _ffi.cast("int*", i.ctypes.data)
  i = cpp_interface.lib.cffi_example(i)

  return i
