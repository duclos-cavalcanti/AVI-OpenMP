## Interface python code for CFFI

## Imports
from cffi import FFI

def compile_interface(verbose:bool = True) -> object:
  ffi = FFI()
  ffi.cdef("""int cffi_example(int i);""")

  ffi.set_source("cpp_interface",
                 """ #include "interface.h" """,
                 include_dirs=['include'],
                 libraries=['cpp_backend_lib'],
                 library_dirs=['lib'],
                 extra_link_args=['-Wl,-rpath=$ORIGIN/lib', '-fopenmp'],
                 extra_compile_args=['-O3', '-march=native', '-ffast-math', '-fopenmp', '-D use_openmp'],
                 source_extension='.cpp')

  return ffi.compile(verbose=verbose)

if __name__ == "__main__":
  compile_interface()
