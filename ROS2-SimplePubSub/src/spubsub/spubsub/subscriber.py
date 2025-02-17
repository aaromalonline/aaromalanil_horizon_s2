import rclpy
from rclpy.node import Node
from std_msgs.msg import String


#creates a node (blueprint) named 'subscriber' to subscribe messages from the topic 'sayhello'
class Subscriber(Node):
    
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription( String,'sayhello',self.listener_callback,10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = Subscriber() #subscriber node object
    rclpy.spin(node) 
    node.destroy_node() 
    rclpy.shutdown()

if __name__ == '__main__':
    main()