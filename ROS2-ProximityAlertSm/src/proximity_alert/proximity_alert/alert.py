import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

ALERT_THRESHOLD = 4.0 # Minimum distance for alert

class Alert(Node):
    def __init__(self):
        super().__init__('alert')
        self.subscription = self.create_subscription(Float32, 'proximity', self.alert_callback, 10) #set subscriber to subscribe to topic 'proximity'
        self.subscription 

    def alert_callback(self, msg):
        distance = msg.data
        if distance < ALERT_THRESHOLD:
            self.get_logger().info(f"ALERT! Object approaching close distance: {distance}m")
        else :
            self.get_logger().info(f"Safe distance: {distance}m")

def main(args=None):
    rclpy.init(args=args)
    node = Alert() #initialized alert node object
    rclpy.spin(node) #keep the node running
    rclpy.shutdown() #shutdown the ROS2 node after the loop(spin)

if __name__ == '__main__':  
    main()