import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator 

import csv
import time
import sys
from datetime import datetime
from threading import Thread


with open("distance_log.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Distance (cm)"])  # Header

time_stamps = []
distances = []


class Alert(Node):
    def __init__(self):
        super().__init__('alert')
        self.subscription = self.create_subscription(Float32, 'proximity', self.alert_callback, 10) #set subscriber to subscribe to topic 'proximity'
        self.subscription 

    def alert_callback(self, msg):

        global time_stamps, distances
        timestamp = datetime.now().strftime("%H:%M:%S")
        distance = msg.data

        #loging data to csv file
        time_stamps.append(timestamp)
        distances.append(distance)

        with open("distance_log.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, distance])

        #alerting based on distance
        if distance < 10:
            self.get_logger().warn(f"\U0001F534 WARNING! Object too close: {distance:.2f} cm")
        elif distance < 30:
            self.get_logger().info(f"\U0001F7E1 CAUTION! Object at: {distance:.2f} cm")
        else:
            self.get_logger().info(f"\U0001F7E2 Safe distance: {distance:.2f} cm")

        #limit data to 50 points
        if len(time_stamps) > 50: 
            time_stamps = time_stamps[-50:]
            distances = distances[-50:]

# Plot realtime distance data (distance vs time)
def update(frame):
    ax.clear()
    ax.plot(time_stamps, distances, marker="o", linestyle="-", color="b")
    ax.axhline(y=10, color="red", linestyle="--", label="Danger (<10 cm)")
    ax.axhline(y=30, color="yellow", linestyle="--", label="Caution (<30 cm)")

    #ax.set_xticks(range(len(time_stamps)))  
    #ax.set_xticklabels(time_stamps, rotation=45, ha="right")
    ax.set_title("Real-Time Distance Monitoring")
    ax.set_ylabel("Distance (cm)")
    ax.set_xlabel("Time")

    ax.xaxis.set_major_locator(MaxNLocator(nbins=10))  # Dynamically manage tick count

    ax.legend()
    ax.grid(True) 


def main():
    rclpy.init(args=None)
    node = Alert() #initialized alert node object

    global fig, ax
    plt.ion() #interactive mode'
    fig, ax = plt.subplots(figsize=(8, 4)) 
    ani = animation.FuncAnimation(fig, update, interval=500)

    ros_thread = Thread(target=rclpy.spin, args=(node,), daemon=True) # Run ROS 2 in a separate thread to keep GUI responsive
    ros_thread.start()

    plt.show(block=True) 
    node.destroy_node()
    rclpy.shutdown() #shutdown the ROS2 node after the loop(spin)

if __name__ == '__main__':
    main()

