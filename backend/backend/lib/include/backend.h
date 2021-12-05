#ifndef _MAIN_H
#define _MAIN_H

#define EIGEN_USE_BLAS
#define EIGEN_USE_LAPACKE

#include <omp.h>
#include <tuple>
#include "Eigen/Sparse" // SparseMatrix manipulations
#include "Eigen/Dense"  // Vector manipulations

typedef Eigen::SparseMatrix<float, Eigen::RowMajor> SparseMat;
typedef std::tuple<int, int, int> state_vector_t;

void asyncValueIterationWrapper(float* val_arr, int* policy_arr, float* values, 
                                int* row_indices, int* rowptr, 
                                const unsigned int nr_nonzero, const unsigned int nr_cols, 
                                const unsigned int nr_rows, const unsigned int nr_stars, 
                                const unsigned int nr_states, const unsigned int nr_actions);

#endif
