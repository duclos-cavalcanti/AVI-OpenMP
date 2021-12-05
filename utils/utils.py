import numpy as np
import pickle

def type_cast(array:np.array, type:str) -> np.array:
  '''
  '''
  if type == "int":
    return array.astype(np.int32)
  if type == "float":
    return array.astype(np.float32)
  if type == "double":
    return array.astype(np.double)

  return array

def load_matrix(path:str, name:str) -> (np.array, np.array, np.array, np.array):
  '''
  '''
  indptr = np.load(f"{path}/{name}_indptr.npy")
  indices = np.load(f"{path}/{name}_indices.npy")
  data = np.load(f"{path}/{name}_data.npy")
  shape = np.load(f"{path}/{name}_shape.npy")
  indptr, indices, data = type_cast(indptr, "int"), type_cast(indices, "int"), type_cast(data, "float")

  return data, indices, indptr, shape

def load_parameters(path:str):
    """
    """
    with open(f"{path}", "rb") as the_file:
        parameters = pickle.load(the_file)

        return parameters

def load_results(path:str) -> (np.array, np.array):
    '''
    '''
    V = np.load(f"{path}/J_star_alpha_0_99.npy")
    PI = np.load(f"{path}/pi_star_alpha_0_99.npy")

    return (V, PI)
