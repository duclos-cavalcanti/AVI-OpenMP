import sys
import numpy as np
import pickle

sys.path.append('backend')

import cpp_backend as backend

def run():
    i = backend.example_func(1)
    print(f"C++ Backend: {i}")

    i = backend.example_func(10)
    print(f"C++ Backend: {i}")

if __name__ == "__main__":
    run()
    with open(f"data/data_debug/parameters.pickle", "rb") as the_file:
        parameters = pickle.load(the_file)
