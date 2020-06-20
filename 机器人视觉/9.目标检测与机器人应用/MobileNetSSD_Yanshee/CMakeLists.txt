cmake_minimum_required(VERSION 2.8.10)
project(MobileNet_Demo)

set(NCNN_LIBS ${CMAKE_SOURCE_DIR}/lib/libncnn.a)
set(NCNN_INCLUDE_DIRS ${CMAKE_SOURCE_DIR}/include)

find_package(OpenMP REQUIRED)
if(OPENMP_FOUND)
    message("OPENMP FOUND")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
endif()

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

include_directories(${NCNN_INCLUDE_DIRS})

add_executable(MobileNetSSD MobileNetSSD.cpp)
target_link_libraries(MobileNetSSD ${NCNN_LIBS} ${OpenCV_LIBS})

