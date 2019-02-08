mkdir -p ~/catkin_ws/src
source "/opt/ros/$ROS_DISTRO/setup.bash"
#cd ~/catkin_ws/src
#catkin_init_workspace
#cd ~/catkin_ws
#catkin_make
#source ~/catkin_ws/devel/setup.bash

roscore &
rosrun gazebo_ros gzserver --verbose
