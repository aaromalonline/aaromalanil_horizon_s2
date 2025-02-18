# ROS2 Simple Publisher and Subscriber

This project demonstrates a simple implementation of a publisher and subscriber nodes using ROS2 Humble. The publisher node sends messages to a 'sayhello' topic, and the subscriber node listens (subscribed) to that topic and processes the messages.

testcase-1 : ./testcase-1.png


## Requirements

- ROS2 Humble on a Ubuntu 22.04 LTS (ros-humble-desktop)
- Python 3.6 or later
 
## Setup Instructions

change directory :

```
cd ./ROS2-SimplePubSub
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