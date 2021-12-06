import sys
import numpy as np
import pickle
import scipy.sparse
from matplotlib import pyplot as plt

sys.path.append('backend')

import cpp_backend as backend
import data_demo as data
import graph

# change to choose between datasets: debug, small, normal
DATASET="debug"

def plot(probabilities, values_result, policies_result, max_fuel, nr_stars, nr_actions):
    random_state = data.state_from_tuple(max_fuel - 1, nr_stars - 1, 0, nr_stars)
    star_graph, stars, star_types = data.load_star_values(f"data/data_{DATASET}")
    fuel, goal_star, cur_star = data.state_to_tuple(random_state, nr_stars)

    a_path = graph.a_star(cur_star, goal_star, star_graph, stars)
    pi_path = data.travel(random_state, probabilities, policies_result, nr_stars, nr_actions)

    data.plot_full_graph(star_graph, stars, star_types, (a_path, "orange"), (pi_path, "red"))
    plt.savefig("plot.png")

    return

def run():
    values, indices, indptr, shape = data.load_sparse_matrix(f"data/data_{DATASET}", "P")
    max_fuel, nr_states, nr_actions, nr_stars = data.load_parameters(f"data/data_{DATASET}/parameters.pickle")

    value_arr = np.zeros(nr_states).astype(np.float32)
    policy_arr = np.zeros(nr_states).astype(np.int32)

    values_result, policies_result = backend.async_value_iteration(value_arr.copy(), policy_arr.copy(), values, indices, indptr, shape, nr_stars, nr_states, nr_actions)

    plot(data.to_sparse_matrix(values, indices, indptr, shape), values_result, policies_result, max_fuel, nr_stars, nr_actions)

    return

if __name__ == "__main__":
    run()
