# Simple Delta Robot Simulation

This repository contains the ROS 2 workspace for the Simple Delta Robot.

## Prerequisites

Ensure you have the following installed:

- **Ubuntu 22.04**
- **ROS 2 Humble**
- **Gazebo classic**

## Clone the Repository

```bash
git clone https://github.com/LevinTamir/simple_delta_robot_ws.git
cd simple_delta_robot_ws
```

## Build the Workspace

1. Source your ROS 2 Humble installation:
   ```bash
   source /opt/ros/humble/setup.bash
   ```

2. Build the workspace using colcon:
   ```bash
   colcon build
   ```

3. Source the workspace after the build:
   ```bash
   source install/setup.bash
   ```

## Run the Delta Robot Simulation

1. Launch the robot description:
   ```bash
   ros2 launch simple_delta_robot_description display.launch.py
   ```

2. Gazebo simulation will be added soon (WIP)


## References

This project leverages the following repositories:

- [gz_attach_links](https://github.com/oKermorgant/gz_attach_links)
- [simple_delta_robot](https://github.com/andy-Chien/simple_delta_robot)


## Contributing

Feel free to submit issues or pull requests to improve the workspace or its documentation.
