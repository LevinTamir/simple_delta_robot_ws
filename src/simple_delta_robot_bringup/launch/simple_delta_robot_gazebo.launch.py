from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
import os
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_path


def generate_launch_description():

    urdf_path = os.path.join(
        get_package_share_path("simple_delta_robot_description"),
        "urdf",
        "delta_robot.xacro",
    )

    rviz_config_path = os.path.join(
        get_package_share_path("simple_delta_robot_bringup"),
        "rviz",
        "bringup_config.rviz",
    )

    gazebo_launch_path = os.path.join(
        get_package_share_path("gazebo_ros") / "launch" / "gazebo.launch.py"
    )

    robot_description = ParameterValue(Command(["xacro ", urdf_path]), value_type=str)

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}],
    )

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_path)
    )

    gazebo_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "delta_robot"],
    )

    rviz2_node = Node(
        package="rviz2", executable="rviz2", arguments=["-d", rviz_config_path]
    )

    return LaunchDescription(
        [robot_state_publisher_node, rviz2_node, gazebo_launch, gazebo_node]
    )
