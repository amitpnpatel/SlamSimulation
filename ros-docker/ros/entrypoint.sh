mkdir -p ~/catkin_ws/src
source /usr/share/gazebo/setup.sh
source "/opt/ros/$ROS_DISTRO/setup.bash"
#cd ~/catkin_ws/src
#catkin_init_workspace
#cd ~/catkin_ws
#catkin_make
#source ~/catkin_ws/devel/setup.bash

#roscore &
#rosrun gazebo_ros gzserver --verbose
gzserver /usr/share/gazebo-9/worlds/single_rotor_demo.world --verbose
#tail -f /dev/null
