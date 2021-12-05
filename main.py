import sys
import numpy as np
import pickle
import scipy.sparse
from matplotlib import pyplot as plt

sys.path.append('backend')
sys.path.append('utils')

import cpp_backend as backend
import utils
import data
import graph

def plot():

    return

def run():
    star_values, star_indices, star_indptr, star_shape = utils.load_matrix("data/data_debug", "star_graph")
    values, indices, indptr, shape = utils.load_matrix("data/data_debug", "P")
    parameters = utils.load_parameters("data/data_debug/parameters.pickle")

    max_fuel = parameters["fuel_capacity"]
    nS, nA = parameters["NS"], parameters["max_controls"]
    n_stars = parameters["number_stars"]

    V = np.zeros(nS).astype(np.float32)
    PI = np.zeros(nS).astype(np.int32)

    values_result, policies_result = backend.async_value_iteration(V.copy(), PI.copy(), values, indices, indptr, shape, n_stars, nS, nA)

    P = scipy.sparse.csr_matrix((values, indices, indptr), shape=shape, dtype=values.dtype)
    star_graph = scipy.sparse.csr_matrix((star_values, star_indices, star_indptr), shape=star_shape, dtype=star_values.dtype)
    stars = np.load("data/data_debug/stars.npy")
    star_types = np.load("data/data_debug/star_types.npy")
    random_state = data.state_from_tuple(max_fuel - 1, n_stars - 1, 0, n_stars)

    fuel = random_state // (n_stars * n_stars)
    goal_star = random_state % (n_stars * n_stars) // n_stars
    cur_star = random_state % (n_stars * n_stars) % n_stars

    a_path = graph.a_star(cur_star, goal_star, star_graph, stars)
    pi_path = data.travel(random_state, P, policies_result, n_stars, nA)
    data.plot_full_graph(star_graph, stars, star_types, (a_path, "orange"), (pi_path, "red"))
    plt.show()


if __name__ == "__main__":
    run()
