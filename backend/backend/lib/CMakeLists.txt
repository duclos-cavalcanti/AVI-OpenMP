cmake_minimum_required(VERSION 3.10 FATAL_ERROR)
project(${LIBRARY_NAME})

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_MODULE_PATH 
    ${CMAKE_MODULE_PATH}
    ${CMAKE_CURRENT_LIST_DIR}/cmake)

set (CMAKE_CXX_STANDARD 11)

# find_package(Threads REQUIRED)
find_package(OpenMP REQUIRED)
find_package(MPI REQUIRED)
find_package(BLAS REQUIRED)     # Basic Linear Algebra Subprogram
find_package(LAPACK REQUIRED)   # Linear Algebra Package
find_package(LAPACKE REQUIRED)  # Eigen muss mit der Lineare Algebra umgehen, Schnitstelle

file(GLOB SOURCES "${CMAKE_CURRENT_LIST_DIR}/src/*.cpp")

set(PROJECT_SOURCES
    ${SOURCES} 
)

set(PROJECT_INCLUDES
    ${PARENT_DIR}/include
    ${CMAKE_CURRENT_LIST_DIR}/include
    ${MPI_INCLUDE_PATH} 
    ${LAPACKE_INCLUDE_DIRS_DEP}   # already done in FindLAPACKE.cmake
)

include_directories(${PROJECT_INCLUDES})

add_library(${PROJECT_NAME} SHARED ${PROJECT_SOURCES})

target_link_libraries(${PROJECT_NAME} 
                      ${MPI_LIBRARIES}
                      ${LAPACKE_LIBRARIES_DEP}
                      OpenMP::OpenMP_CXX
                      )

install(DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/include 
        DESTINATION ${BACKEND_DIR}
        MESSAGE_NEVER FILES_MATCHING PATTERN "*"
        )

install(TARGETS ${PROJECT_NAME}
        LIBRARY DESTINATION ${BACKEND_DIR}/lib
        CONFIGURATIONS Release
        )

