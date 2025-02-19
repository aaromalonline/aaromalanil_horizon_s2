# ROS2 : Proximity Alert System (Stimulation)

A virtual security system using ROS 2 that simulates motion detection & analysis using simple publisher & subscribtion nodes. The sensor node publishes distance values from the sensor (here generated random) to a topic /proximity where the alert node subscribes to. The alert node could analayse & check whether the distances received pass a specific threshold thus alerting based on that. The project can be scaled to receive real data from a ultrasonic sensor on microcontroller board and communicate with nodes of ROS2 using microros system.


## Features

- Sensor node read/randomly generate distance data & publish it into proximity topic
- Alert node receive distances from its subscribed topic proximity
- Log out warning mesaages on terminal and csv file based on obstacle distances in realtime
- Analyse and plot the relatime distances vs time of the obstacle

## Directory Structure

ROS2 package : proximity_alert
nodes : sensor, alert

```
/ROS2-ProximityAlertSm
├── src/                       
│   ├── proximity_alert/             
│   │   ├── proximity_alert/        
│   │   │   ├── __init__.py   
│   │   │   ├── sensor.py   
│   │   │   ├── alert.py  
│   │   ├── resource/   
│   │   ├── test/        
│   │   ├── setup.py           
│   │   ├── package.xml        
│   │   ├── setup.cfg           
├── testcase-1.png 
├── testcase-2.webm
├── requirements.txt                        
├── README.md                              
```

## Requirements

- ROS2 Humble on a Ubuntu 22.04 LTS (ros-humble-desktop)
- Python 3.6 or later
 
## Setup Instructions

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
colcon build --packages-select proximity_alert
```

### 4. Run the Nodes

Open a new terminal for each node and source the env

```bash
source ros2_env/bin/activate
source install/setup.bash
```

To run the publisher node (sensor):

```bash
ros2 run proximity_alert sensor
```

To run the subscription node (alert):

```bash
ros2 run proximity_alert alert
```
