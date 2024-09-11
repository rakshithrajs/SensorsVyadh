import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    # Define the node to launch Foxglove Bridge
    foxglove_bridge_node = Node(
        package="foxglove_bridge",
        executable="foxglove_bridge",
        name="foxglove_bridge",
        output="screen",
    )

    # Define the process to launch Foxglove Studio via snap
    foxglove_studio_process = ExecuteProcess(
        cmd=[
            "snap",
            "run",
            "foxglove-studio",
        ],  # Use the snap command to launch the application
        output="screen",
    )

    return LaunchDescription(
        [
            foxglove_bridge_node,
            foxglove_studio_process,
        ]
    )
