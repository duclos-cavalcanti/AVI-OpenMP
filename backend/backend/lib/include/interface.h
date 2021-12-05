#ifndef _INTERFACE_BACKEND_CPP_H
#define _INTERFACE_BACKEND_CPP_H

#include "main.h"

extern "C"
{
  extern void async_value_iteration(float* V, int* PI, float* values, 
                                    int* row_indices, int* rowptr, 
                                    const unsigned int nnz, const unsigned int cols, 
                                    const unsigned int rows, const unsigned int n_stars, 
                                    const unsigned int nS, const unsigned int nA)
  {
    asyncValueIterationWrapper(V, PI, values, 
                               row_indices, rowptr, 
                               nnz, cols, 
                               rows, n_stars, 
                               nS, nA);
  }
}

#endif
