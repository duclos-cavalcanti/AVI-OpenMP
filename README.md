# Asynchronous Value Iteration with OpenMPI

An example of the use of asynchronous value iteration to find an optimal path between two
points. A backend written in `C++` is bridged with a `Python` API with help of the `CFFI`
interface. The `Python` frontend reads the data stored as numpy arrays and passes it on to
the `C++` wrappers which compute the trajectory. Finally with the given trajectory, an
image is plotted of the solution.

## Targets
- clean : cleans project
- compile : compiles project
- test : runs functional tests (needs to compile beforehand)


## Tools
- `CMake`: Build and Automation Tool
- `CFFI` : C Foreign Function Interface, bridges C++ and Python
- `Pytest`: Unit testing
- Libraries
    - `BLAS`
    - `LAPACK`
    - `LAPACKE`
    - `OpenMP`

### Arch-based Systems
```sh
sudo pacman -S cmake openmpi lapack lapacke
pip install cffi pytest
```
