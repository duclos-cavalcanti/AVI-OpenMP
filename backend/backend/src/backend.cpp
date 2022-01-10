#include "backend.h"
#include <iostream>
#include <cmath>

void asyncValueIteration(Eigen::Ref<Eigen::VectorXf> V, Eigen::Ref<Eigen::VectorXi> PI, Eigen::Ref<SparseMat> probabilities, const unsigned int n_stars, const unsigned int nS, const unsigned int nA);
inline void getStateCost(float& cost, int& state, int& control, const unsigned int& nr_stars);
inline Eigen::VectorXf getActionValues(Eigen::Ref<SparseMat> probabilities, Eigen::Ref<Eigen::Map<Eigen::VectorXf>> values, int current_state, const unsigned int& nr_actions, const unsigned int& nr_stars, const float& alpha);

void asyncValueIterationWrapper(float* val_arr, int* policy_arr, float* values, 
                                int* row_indices, int* rowptr, 
                                const unsigned int nr_nonzero, const unsigned int nr_cols, 
                                const unsigned int nr_rows, const unsigned int nr_stars, 
                                const unsigned int nr_states, const unsigned int nr_actions) {

  Eigen::Map<Eigen::VectorXf> value_map(val_arr, nr_states);
  Eigen::Map<Eigen::VectorXi> policy_map(policy_arr, nr_states);
  Eigen::Map<SparseMat> probabilities_map(nr_rows, nr_cols, nr_nonzero, rowptr, row_indices, values);

  asyncValueIteration(value_map, policy_map, probabilities_map, nr_stars, nr_states, nr_actions);
}

void asyncValueIteration(Eigen::Ref<Eigen::VectorXf> values, 
                         Eigen::Ref<Eigen::VectorXi> policies, 
                         Eigen::Ref<SparseMat> probabilities, 
                         const unsigned int nr_stars, 
                         const unsigned int nr_states, 
                         const unsigned int nr_actions) {

    omp_set_num_threads(4);

    const double tolerance = 1e-6;
    const float alpha = 0.99;
    float delta;
    unsigned int epochs = 0;
    unsigned int max_iter = 1e3;

    do {
      delta = 0;
      #pragma omp parallel for
      for (unsigned int current_state = 0; current_state < nr_states; current_state++) {
        Eigen::VectorXf action_values = getActionValues(probabilities, values, current_state, nr_actions, nr_stars, alpha);

        Eigen::VectorXi::StorageIndex min_index;
        float min_value = action_values.minCoeff(&min_index);

        delta = std::max(delta, std::abs(min_value - values[current_state]));

        values[current_state] = min_value;
        policies[current_state] = min_index; // action needed to achieve min value
      }
      epochs += 1;

      if (epochs >= max_iter)
        break;

    } while (delta >= tolerance);
}

inline Eigen::VectorXf getActionValues(Eigen::Ref<SparseMat> probabilities, 
                                       Eigen::Ref<Eigen::Map<Eigen::VectorXf>> values, 
                                       int current_state, 
                                       const unsigned int& nr_actions, 
                                       const unsigned int& nr_stars, 
                                       const float& alpha) {
  const auto& probabilities_slice = probabilities.middleRows(current_state * nr_actions, nr_actions);
  int actions = 0;
  for (unsigned int i = 0; i < nr_actions; i++)
      if (probabilities_slice.row(i).sum() > 0)
          actions += 1;
  
  Eigen::VectorXf action_values(actions);
  action_values.fill(0.0);

  #pragma omp parallel for
  for (int row = 0; row < probabilities_slice.outerSize(); ++row) {
    for (Eigen::InnerIterator<typeof(probabilities_slice)> it(probabilities_slice, row); it; ++it) { // iterates columns
      float cost;
      float probability = it.value();
      int next_state = it.col();
      int current_action = it.row();
      getStateCost(cost, current_state, current_action, nr_stars);
      action_values[current_action] += probability * (cost + alpha * values[next_state]);
      }
    }

  return action_values;
}

// calculates cost attributed to a given state and a given action
// stores directly in cost pointer
inline void getStateCost(float& cost, int& state, int& control, const unsigned int& nr_stars) {
    state_vector_t state_vector;
    int fuel, goal_star, current_star;
    
    std::get<0>(state_vector) = state / (nr_stars * nr_stars);
    std::get<1>(state_vector) = state % (nr_stars * nr_stars) / nr_stars;
    std::get<2>(state_vector) = state % (nr_stars * nr_stars) % nr_stars;

    std::tie(fuel, goal_star, current_star) = state_vector;

    if (goal_star == current_star && control == 0) {
        cost = -100.0;
    } else if (fuel == 0) {   // out of fuel
        cost = 100.0;
    } else if (control > 0) { // avoid unnecessary jumps
        cost = 5.0;
    } else {                  // else no cost
        cost = 0.0;
    }
  }
