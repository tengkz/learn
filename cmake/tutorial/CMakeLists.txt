cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(SumTwo VERSION 1.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# should we use our own math functions
option(USE_MYMATH "Use tutorial provided math implementation" OFF)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file(SumTwoConfig.h.in SumTwoConfig.h)

# add the MathFunction library
if(USE_MYMATH)
    add_subdirectory(MathFunctions)
    list(APPEND EXTRA_LIBS MathFunctions)
endif()

# add the executable
add_executable(SumTwo SumTwo.cxx)

target_link_libraries(SumTwo PUBLIC ${EXTRA_LIBS})

# add the binary tree to the search path for include files
# so that we will find SumTwoConfig.h
target_include_directories(SumTwo PUBLIC 
                           "${PROJECT_BINARY_DIR}"
                          )
