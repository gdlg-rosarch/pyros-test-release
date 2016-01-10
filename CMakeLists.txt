cmake_minimum_required(VERSION 2.8.3)
project(pyros_test)

# Minimal Python module setup
find_package(catkin REQUIRED COMPONENTS
    roslint
    rospy
    std_msgs
    message_generation
)

catkin_python_setup()

add_service_files(DIRECTORY srv
    FILES
    StringEchoService.srv
)
generate_messages(DEPENDENCIES std_msgs)
catkin_package( CATKIN_DEPENDS message_runtime std_msgs)

install(
    PROGRAMS
        nodes/echo.py
        nodes/emptyService.py
        nodes/slowService.py
        nodes/triggerService.py
        nodes/common.py
        nodes/string_pub_node.py
        nodes/string_pubnot_node.py
        nodes/string_slow_node.py
        nodes/string_sub_node.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
    )

# Lint Python modules
file(GLOB_RECURSE ${PROJECT_NAME}_PY_SRCS
     RELATIVE ${PROJECT_SOURCE_DIR} src/pyros_test/*.py)
roslint_python(${${PROJECT_NAME}_PY_SRCS})

