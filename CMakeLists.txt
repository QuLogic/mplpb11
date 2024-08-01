cmake_minimum_required(VERSION 3.28)
set(CMAKE_CXX_STANDARD 17)

project(mplpb11 CXX)
message(STATUS "CMAKE_CXX_COMPILER_ID: ${CMAKE_CXX_COMPILER_ID}")
message(STATUS "CMAKE_CXX_COMPILER_VERSION: ${CMAKE_CXX_COMPILER_VERSION}")
message(STATUS "CMAKE_CXX_COMPILER: ${CMAKE_CXX_COMPILER}")
set(CMAKE_BUILD_TYPE "RELEASE")
message(STATUS "CMAKE_BUILD_TYPE: ${CMAKE_BUILD_TYPE}")
add_library(cxxerror error.cpp error.hpp)
set_target_properties(cxxerror PROPERTIES POSITION_INDEPENDENT_CODE TRUE)

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(_pyerror main.cpp)
target_link_libraries(_pyerror PRIVATE cxxerror)


if(NOT CMAKE_LIBRARY_OUTPUT_DIRECTORY)
    set_target_properties(_pyerror PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR})
    foreach(config ${CMAKE_CONFIGURATION_TYPES})
        string(TOUPPER ${config} config)
        set_target_properties(_pyerror PROPERTIES
                LIBRARY_OUTPUT_DIRECTORY_${config} ${CMAKE_SOURCE_DIR})
    endforeach()
endif()
