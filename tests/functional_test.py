import pytest
import sys
import numpy as np
import pickle

sys.path.append('backend')

import cpp_backend as backend
import data_demo as data


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

    values_result, policies_result = backend.async_value_iteration(value_arr.copy(), policy_arr.copy(), values, indices, indptr, shape, nr_stars, nr_states, nr_actions)
    values_golden, policies_golden = data.load_results("data/data_debug")

    assert values_result.all() == values_golden.all(), "Values do not match golden debug values"
    assert policies_result.all() == policies_golden.all(), "Results do not match golden debug results"

    print(values_result)
    print(values_golden)
    print(policies_result)
    print(policies_golden)

    return
