cmake_minimum_required(VERSION 3.10 FATAL_ERROR)
project(backend_debug)

set (BACKEND_NAME backend)
set (BACKEND_DIR ${PROJECT_SOURCE_DIR}/..)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

set (CMAKE_CXX_STANDARD 11)

# find_package(MPI REQUIRED)
find_package(OpenMP REQUIRED)
find_package(BLAS REQUIRED)     # Basic Linear Algebra Subprogram
find_package(LAPACK REQUIRED)   # Linear Algebra Package
find_package(LAPACKE REQUIRED)  # Eigen has to interface with Lineare Algebra

if( ${CMAKE_BINARY_DIR} STREQUAL ${PROJECT_SOURCE_DIR} )
  Message(FATAL_ERROR "Source and build directories are the same!")
endif()

set(CMAKE_CXX_FLAGS 
    ${CMAKE_CXX_FLAGS} 
    "-Wall -O0 -g"
    )

set(CMAKE_CXX_FLAGS_RELEASE 
    "-O3 -ffast-math -fopenmp"
    )

set(CMAKE_EXE_LINKER_FLAGS  
    "${CMAKE_EXE_LINKER_FLAGS}")

file(GLOB SOURCES "${PROJECT_SOURCE_DIR}/src/*.cpp")

set(PROJECT_SOURCES
    ${SOURCES} 
)

set(BACKEND_SOURCES
    ${SOURCES} 
)

list(REMOVE_ITEM 
     BACKEND_SOURCES 
     ${PROJECT_SOURCE_DIR}/src/main.cpp)

set(PROJECT_INCLUDES
    # ${MPI_INCLUDE_PATH} 
    ${PROJECT_SOURCE_DIR}/lib/Eigen
    ${PROJECT_SOURCE_DIR}/lib/
    ${PROJECT_SOURCE_DIR}/include/
    ${LAPACKE_INCLUDE_DIRS_DEP}
)

include_directories(${PROJECT_INCLUDES})

add_executable(${PROJECT_NAME} ${PROJECT_SOURCES})
target_link_libraries(${PROJECT_NAME})

add_library(${BACKEND_NAME} SHARED ${BACKEND_SOURCES})
target_link_libraries(${BACKEND_NAME} 
                      # ${MPI_LIBRARIES}
                      ${LAPACKE_LIBRARIES_DEP}
                      OpenMP::OpenMP_CXX
                      )

# install(DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/include 
#         DESTINATION ${BACKEND_DIR}
#         MESSAGE_NEVER FILES_MATCHING PATTERN "*"
#         )

install(TARGETS ${BACKEND_NAME}
        LIBRARY DESTINATION ${BACKEND_DIR}/lib
        CONFIGURATIONS Release
        )

# extra cmake targets and scripts
include(run)
include(gdb)
