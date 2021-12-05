## Interface python code for CFFI

## Imports
from cffi import FFI

def compile_interface(verbose:bool = True) -> object:
  ffi = FFI()
  ffi.cdef("""void asyncValueIteration(float* V, int* PI, float* values, int* row_indices, int* rowptr, const unsigned int nnz, const unsigned int cols, const unsigned int rows, const unsigned int n_stars, const unsigned int nS, const unsigned int nA);""")

  ffi.set_source("cpp_interface",
                 """ #include "interface.h" """,
                 include_dirs=['include'],
                 libraries=['backend'],
                 library_dirs=['lib'],
                 extra_link_args=['-Wl,-rpath=$ORIGIN/lib', '-fopenmp'],
                 extra_compile_args=['-O3', '-march=native', '-ffast-math', '-fopenmp', '-D use_openmp'],
                 source_extension='.cpp')

  return ffi.compile(verbose=verbose)

if __name__ == "__main__":
  compile_interface()
