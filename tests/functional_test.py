import pytest
import sys
import numpy as np
import pickle

sys.path.append('backend')
sys.path.append('utils')

import cpp_backend as backend
import utils


def test_debug_data():
    """Description

    @param param:  Description
    @type  param:  Type

    @return:  Description
    """
    values, indices, indptr, shape = utils.load_matrix("data/data_debug", "P")
    parameters = utils.load_parameters("data/data_debug/parameters.pickle")

    nS, nA = parameters["NS"], parameters["max_controls"]
    n_stars = parameters["number_stars"]

    V = np.zeros(nS).astype(np.float32)
    PI = np.zeros(nS).astype(np.int32)

    values_result, policies_result = backend.async_value_iteration(V.copy(), PI.copy(), values, indices, indptr, shape, n_stars, nS, nA)
    values_golden, policies_golden = utils.load_results("data/data_debug")

    assert values_result.all() == values_golden.all(), "Values do not match golden values"
    assert policies_result.all() == policies_golden.all(), "Results do not match golden results"

    return
