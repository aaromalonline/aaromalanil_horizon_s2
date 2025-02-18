import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#creates a node (blueprint) named 'publisher' to publish messages to the topic 'sayhello'
class Publisher(Node): #inherited from Node Class
    def __init__(self):
        super().__init__('publisher')
        self.publisher = self.create_publisher(String, 'sayhello', 10) #set topic as 'sayhello'
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self): #publishes message to the topic 'sayhello', internally called by timer
        msg = String()
        msg.data = 'Hello, World!'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Publisher() #node object
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
