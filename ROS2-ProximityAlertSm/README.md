# ROS2 : Proximity Alert System (Stimulation)

A virtual security system using ROS 2 that simulates motion detection using simple publisher & subscriber nodes. A sensor node publishes distance values, and an alert node checks if the distance is below a threshold. If an object is too close, it triggers an alarm (printed warning + optional sound).

Use Case: This can simulate real-world security systems where a motion sensor detects intruders and triggers an alarm. This can be implimented using arduino and microros s/m where arduino itself acts as sensor node and publishes the distances from a ultrasonic sensor (proximity) to a topic whhere the alert subscribes to anlyse and trigger the alarm. ROS implimentation is more effective and scalable compared to plane code implimentation.

testcase-1 : ./testcase-1.png


## Requirements

- ROS2 Humble on a Ubuntu 22.04 LTS (ros-humble-desktop)
- Python 3.6 or later
 
# Setup Instructions

change directory :

```
cd ./ROS2-ProximityAlertSm
```

### 1. Initialize a Virtual Environment

```bash
python3 -m venv ros2_env
source ros2_env/bin/activate
```

### 2. Install Required Modules

```bash
pip install -r requirements.txt
```

### 3. Build the Project

```bash
colcon build --packages-select spubsub
```

### 4. Run the Nodes

Open a new terminal for each node and source the env

```bash
source ros2_env/bin/activate
source install/setup.bash
```

To run the publisher node:

```bash
ros2 run spubsub publisher
```

To run the subscriber node:

```bash
ros2 run spubsub subscriber
```