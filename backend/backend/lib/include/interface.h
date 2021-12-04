#ifndef _INTERFACE_BACKEND_CPP_H
#define _INTERFACE_BACKEND_CPP_H

#include "example.h"

extern "C"
{
  extern int cffi_example(int i)
  {
    return example_func(i);
  }
}

#endif
