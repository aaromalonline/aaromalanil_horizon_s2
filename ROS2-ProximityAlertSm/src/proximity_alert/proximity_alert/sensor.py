import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random
import time

#blueprint for the sensor node
class Sensor(Node):
    def __init__(self):
        super().__init__('sensor')
        self.publisher = self.create_publisher(Float32, 'proximity', 10) #set publisher to publish data to topic 'proximity'
        self.timer = self.create_timer(1, self.publish_distance) 

    def publish_distance(self):
        distance = random.uniform(1.0, 10.0)
        msg = Float32()
        msg.data = distance
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing distance: {distance}m")

def main(args=None):
    rclpy.init(args=args)
    node = Sensor() #initialized sensor node object
    rclpy.spin(node) #keep the node running
    rclpy.shutdown() #shutdown the ROS2 node after the loop(spin)

if __name__ == '__main__':  
    main()