#ifndef _INTERFACE_BACKEND_CPP_H
#define _INTERFACE_BACKEND_CPP_H

#include "backend.h"

extern "C"
{
  extern void async_value_iteration(float* val_arr, int* policy_arr, float* values, 
                                    int* row_indices, int* rowptr, 
                                    const unsigned int nr_nonzero, const unsigned int nr_cols, 
                                    const unsigned int nr_rows, const unsigned int nr_stars, 
                                    const unsigned int nr_states, const unsigned int nr_actions)
  {
    asyncValueIterationWrapper(val_arr, policy_arr, values, 
                               row_indices, rowptr, 
                               nr_nonzero, nr_cols, 
                               nr_rows, nr_stars, 
                               nr_states, nr_actions);
  }
}

#endif
