import importlib.util ## to be able to load backend package from different folder source

spec = importlib.util.spec_from_file_location("*", "backend/backend_py.py") ## load python backend from backend folder
b = importlib.util.module_from_spec(spec) ## import backend
spec.loader.exec_module(b) ## import backend

from backend import * ## import both backends

def run():
    i_py = backend_py.example_func(2)
    i_cpp = backend.example_func(1)

    print(f"Python backend: {i_py} and C++ Backend: {i_cpp}")

if __name__ == "__main__":
    run()
