# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.7

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/Desktop/MobileNet_me

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/Desktop/MobileNet_me/build

# Include any dependencies generated for this target.
include CMakeFiles/MobileNetSSD.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/MobileNetSSD.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/MobileNetSSD.dir/flags.make

CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o: CMakeFiles/MobileNetSSD.dir/flags.make
CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o: ../MobileNetSSD.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/Desktop/MobileNet_me/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o -c /home/pi/Desktop/MobileNet_me/MobileNetSSD.cpp

CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/Desktop/MobileNet_me/MobileNetSSD.cpp > CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.i

CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/Desktop/MobileNet_me/MobileNetSSD.cpp -o CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.s

CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o.requires:

.PHONY : CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o.requires

CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o.provides: CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o.requires
	$(MAKE) -f CMakeFiles/MobileNetSSD.dir/build.make CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o.provides.build
.PHONY : CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o.provides

CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o.provides.build: CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o


# Object files for target MobileNetSSD
MobileNetSSD_OBJECTS = \
"CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o"

# External object files for target MobileNetSSD
MobileNetSSD_EXTERNAL_OBJECTS =

MobileNetSSD: CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o
MobileNetSSD: CMakeFiles/MobileNetSSD.dir/build.make
MobileNetSSD: ../lib/libncnn.a
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_videostab.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_ts.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_superres.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_stitching.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_ocl.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_gpu.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_contrib.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_photo.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_legacy.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_video.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_objdetect.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_ml.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_calib3d.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_features2d.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_highgui.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_imgproc.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_flann.so.2.4.9
MobileNetSSD: /usr/lib/arm-linux-gnueabihf/libopencv_core.so.2.4.9
MobileNetSSD: CMakeFiles/MobileNetSSD.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/Desktop/MobileNet_me/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable MobileNetSSD"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MobileNetSSD.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/MobileNetSSD.dir/build: MobileNetSSD

.PHONY : CMakeFiles/MobileNetSSD.dir/build

CMakeFiles/MobileNetSSD.dir/requires: CMakeFiles/MobileNetSSD.dir/MobileNetSSD.cpp.o.requires

.PHONY : CMakeFiles/MobileNetSSD.dir/requires

CMakeFiles/MobileNetSSD.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/MobileNetSSD.dir/cmake_clean.cmake
.PHONY : CMakeFiles/MobileNetSSD.dir/clean

CMakeFiles/MobileNetSSD.dir/depend:
	cd /home/pi/Desktop/MobileNet_me/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/Desktop/MobileNet_me /home/pi/Desktop/MobileNet_me /home/pi/Desktop/MobileNet_me/build /home/pi/Desktop/MobileNet_me/build /home/pi/Desktop/MobileNet_me/build/CMakeFiles/MobileNetSSD.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/MobileNetSSD.dir/depend

