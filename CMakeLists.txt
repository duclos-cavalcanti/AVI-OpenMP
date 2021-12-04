cmake_minimum_required(VERSION 3.10 FATAL_ERROR)

project(HA)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

set (CMAKE_CXX_STANDARD 11)

if( ${CMAKE_BINARY_DIR} STREQUAL ${PROJECT_SOURCE_DIR} )
  Message( FATAL_ERROR "Source and build directories are the same!")
endif()

# find_package(Threads REQUIRED)
find_package(OpenMP REQUIRED)
find_package(MPI REQUIRED)
find_package(ZLIB REQUIRED)
find_package(BLAS REQUIRED)     # Basic Linear Algebra Subprogram
find_package(LAPACK REQUIRED)   # Linear Algebra Package
find_package(LAPACKE REQUIRED)  # Eigen muss mit der Lineare Algebra umgehen, Schnitstelle

set(CMAKE_CXX_FLAGS 
    ${CMAKE_CXX_FLAGS} 
    -march=native               # compile for the native arch, faster code
    -fast-math                  # allows unsage match operations, faster code
    -fopenmp                    # activates open mp support
    -O0)

set(CMAKE_EXE_LINKER_FLAGS  
    "${CMAKE_EXE_LINKER_FLAGS}")

file(GLOB SOURCES "src/*.cpp")

set(PROJECT_SOURCES
    ${SOURCES} 
)

set(PROJECT_INCLUDES
    ${PROJECT_SOURCE_DIR}/include/
    ${PROJECT_SOURCE_DIR}/lib/include
    ${MPI_INCLUDE_PATH} 
    ${ZLIB_INCLUDE_DIRS} 
    ${LAPACKE_INCLUDE_DIRS_DEP}   # already done in FindLAPACKE.cmake
)

include_directories(${PROJECT_INCLUDES})

add_executable(${PROJECT_NAME} ${PROJECT_SOURCES})

target_link_libraries(${PROJECT_NAME} 
                      ${MPI_LIBRARIES}
                      ${ZLIB_LIBRARIES}
                      ${LAPACKE_LIBRARIES_DEP}
                      OpenMP::OpenMP_CXX
                      pthread
                      )

# Logging mode
if(LOG)
    add_definitions(-DLOGGING)
endif()

# extra cmake targets and scripts
include(run)
include(gdb)
include(deliver)

# clean target files
set_property (DIRECTORY PROPERTY ADDITIONAL_CLEAN_FILES
    "${PROJECT_SOURCE_DIR}/build/CMakeFiles"
    "${PROJECT_SOURCE_DIR}/build/CMakeCache.txt"
    "${PROJECT_SOURCE_DIR}/build/Makefile"
    "${PROJECT_SOURCE_DIR}/build/cmake_install.cmake"
    "${PROJECT_SOURCE_DIR}/build/compile_commands.json"
    )
