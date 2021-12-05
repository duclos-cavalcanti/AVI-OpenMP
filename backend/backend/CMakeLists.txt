cmake_minimum_required(VERSION 3.10 FATAL_ERROR)
project(CPP_BACKEND)

set (LIBRARY_NAME backend)
set (BACKEND_DIR ${PROJECT_SOURCE_DIR}/../)
add_subdirectory(lib) # builds lib project

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

set (CMAKE_CXX_STANDARD 11)

if( ${CMAKE_BINARY_DIR} STREQUAL ${PROJECT_SOURCE_DIR} )
  Message( FATAL_ERROR "Source and build directories are the same!")
endif()

set(CMAKE_CXX_FLAGS 
    ${CMAKE_CXX_FLAGS} 
    "-Wall -O0"
    )

set(CMAKE_CXX_FLAGS_RELEASE 
    "-O3 -march=native -ffast-math -fopenmp"
    )

set(CMAKE_EXE_LINKER_FLAGS  
    "${CMAKE_EXE_LINKER_FLAGS}")

set(SOURCES "main.cpp")

set(PROJECT_SOURCES
    ${SOURCES} 
)

set(PROJECT_INCLUDES
    ${PROJECT_SOURCE_DIR}/lib/include
)

include_directories(${PROJECT_INCLUDES})

add_executable(${PROJECT_NAME} ${PROJECT_SOURCES})

target_link_libraries(${PROJECT_NAME} ${LIBRARY_NAME})

# extra cmake targets and scripts
include(run)
include(gdb)
