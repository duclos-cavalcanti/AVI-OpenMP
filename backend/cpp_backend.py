import numpy as np
import os, logging
from cffi import FFI

try:
  import cpp_interface

except (ModuleNotFoundError, ImportError) as e:
  print(f"Importing of Backend failed.\nReason:\n{e}\n")
  raise

#########################
# Wrappers for c++ code #
#########################

def example_func(i:int) -> (int):
  """
  C++ version backend
  """
  i = cpp_interface.lib.cffi_example(i)

  return i
