import pytest
import sys
import numpy as np
import pickle

sys.path.append('backend')

import cpp_backend as backend
import data_demo as data
import graph


def test_debug_data():
    """Description

    @param param:  Description
    @type  param:  Type

    @return:  Description
    """
    values, indices, indptr, shape = data.load_sparse_matrix("data/data_debug", "P")
    max_fuel, nr_states, nr_actions, nr_stars = data.load_parameters("data/data_debug/parameters.pickle")

    value_arr = np.zeros(nr_states).astype(np.float32)
    policy_arr = np.zeros(nr_states).astype(np.int32)

    # J,pi
    values_result, policies_result = backend.async_value_iteration(value_arr.copy(), policy_arr.copy(), values, indices, indptr, shape, nr_stars, nr_states, nr_actions)
    # J_star,pi_star
    values_golden, policies_golden = data.load_results("data/data_debug")

    assert values_result.all() == values_golden.all(), "Values do not match golden debug values"
    assert policies_result.all() == policies_golden.all(), "Results do not match golden debug results"

    random_state = data.state_from_tuple(max_fuel - 1, nr_stars - 1, 0, nr_stars)
    star_graph, stars, star_types = data.load_star_values(f"data/data_debug")
    fuel, goal_star, cur_star = data.state_to_tuple(random_state, nr_stars)

    a_path = graph.a_star(cur_star, goal_star, star_graph, stars)
    pi_path = data.travel(random_state, data.to_sparse_matrix(values, indices, indptr, shape), policies_result, nr_stars, nr_actions)

    assert a_path[0] == pi_path[0], "Start Values don't match"
    assert a_path[-1] == pi_path[-1], "End Values don't match"

    # (J - J_star).max()
    # distance = np.abs(J - J_star).max()
    distance = np.abs(values_result - values_golden).max()
    assert distance < 1e-3, f"The fixed point is too far away: {distance}"

    return

def test_small_data():
    """Description

    @param param:  Description
    @type  param:  Type

    @return:  Description
    """
    values, indices, indptr, shape = data.load_sparse_matrix("data/data_small", "P")
    max_fuel, nr_states, nr_actions, nr_stars = data.load_parameters("data/data_small/parameters.pickle")

    value_arr = np.zeros(nr_states).astype(np.float32)
    policy_arr = np.zeros(nr_states).astype(np.int32)

    # J,pi
    values_result, policies_result = backend.async_value_iteration(value_arr.copy(), policy_arr.copy(), values, indices, indptr, shape, nr_stars, nr_states, nr_actions)
    # J_star,pi_star
    values_golden, policies_golden = data.load_results("data/data_small")

    random_state = data.state_from_tuple(max_fuel - 1, nr_stars - 1, 0, nr_stars)
    star_graph, stars, star_types = data.load_star_values(f"data/data_small")
    fuel, goal_star, cur_star = data.state_to_tuple(random_state, nr_stars)

    a_path = graph.a_star(cur_star, goal_star, star_graph, stars)
    pi_path = data.travel(random_state, data.to_sparse_matrix(values, indices, indptr, shape), policies_result, nr_stars, nr_actions)

    assert a_path[0] == pi_path[0], "Start Values don't match"
    assert a_path[-1] == pi_path[-1], "End Values don't match"

    # (J - J_star).max()
    # distance = np.abs(J - J_star).max()
    distance = np.abs(values_result - values_golden).max()
    assert distance < 1e-3, f"The fixed point is too far away: {distance}"

    return
