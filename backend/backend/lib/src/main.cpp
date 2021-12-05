#include "main.h"
#include <iostream>
#include <cmath>
#include <chrono>

void asyncValueIteration(Eigen::Map<Eigen::VectorXf> V, Eigen::Map<Eigen::VectorXi> PI, Eigen::Map<SparseMat> probabilities, const unsigned int n_stars, const unsigned int nS, const unsigned int nA);

void asyncValueIterationWrapper(float* V, int* PI, float* values, 
                                int* row_indices, int* rowptr, 
                                const unsigned int nnz, const unsigned int cols, 
                                const unsigned int rows, const unsigned int n_stars, 
                                const unsigned int nS, const unsigned int nA) {

  Eigen::Map<Eigen::VectorXf> v_map(V, nS);
  Eigen::Map<Eigen::VectorXi> pi_map(PI, nS);
  Eigen::Map<SparseMat> probabilities_map(rows, cols, nnz, rowptr, row_indices, values);

  asyncValueIteration(v_map, pi_map, probabilities_map, n_stars, nS, nA);
}

void asyncValueIteration(Eigen::Map<Eigen::VectorXf> V, 
                         Eigen::Map<Eigen::VectorXi> PI, 
                         Eigen::Map<SparseMat> probabilities, 
                         const unsigned int n_stars, const unsigned int nS, const unsigned int nA)
  {

  }

