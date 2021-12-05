#ifndef _EXAMPLE_BACKEND_CPP_H
#define _EXAMPLE_BACKEND_CPP_H

#define EIGEN_USE_BLAS
#define EIGEN_USE_LAPACKE

#include <omp.h>
#include "Eigen/Sparse" // SparseMatrix manipulations
#include "Eigen/Dense"  // Vector manipulations

typedef Eigen::SparseMatrix<float, Eigen::RowMajor> SparseMat;

void asyncValueIterationWrapper(float* V, int* PI, float* values, 
                                int* row_indices, int* rowptr, 
                                const unsigned int nnz, const unsigned int cols, 
                                const unsigned int rows, const unsigned int n_stars, 
                                const unsigned int nS, const unsigned int nA);

#endif
