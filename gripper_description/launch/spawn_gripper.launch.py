from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():

    pkg_path = get_package_share_directory('gripper_description')
    xacro_file = os.path.join(pkg_path, 'urdf', 'gripper.urdf.xacro')
    controllers_file = os.path.join(pkg_path, 'config', 'controllers.yaml')

    robot_desc = xacro.process_file(xacro_file).toxml()

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}],
        ),

        ExecuteProcess(
        cmd=['ros2', 'run', 'ros_ign_gazebo', 'create',
               '-name', 'gripper',
               '-topic', 'robot_description'],
          output='screen'
        ),
    ])