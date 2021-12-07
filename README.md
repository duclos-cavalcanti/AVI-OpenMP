# Dynamic Programming with OpenMPI

## Introduction

The `cpp_backend` is located nested in the `backend` folder.

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
    - `OpenMPI`

### Arch-based Systems
```sh
sudo pacman -S cmake openmpi lapack lapacke
pip install cffi pytest
```
### Debian-based Systems
```sh
# TODO
```
