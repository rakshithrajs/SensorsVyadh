import rclpy
from rclpy.node import Node
from std_msgs.msg import String



class aujvfcj(Node):
    def __init__(self):
        super().__init__("sample_node")
        # self.subsa = self.create_subscription(String, "arduino_data", self.caller, 10)
        # global IR_sensor_data, US_sensor_data
        # IR_sensor_data = []
        # US_sensor_data = []
        # global sensors
        # sensors = {}
        # self.sensor = self.create_service(Trigger, "get_avg_data", self.button_clicked)
        self.publisher = self.create_publisher(String, "/topic" , 10)
        self.create_timer(1, self.s)
        self.get_logger().info("turtlebot3_cntrlr node created")
        
    def s(self):
        msg = String()
        msg.data = "dhenge"
        self.publisher.publish(msg)
        

    


def main(args=None):
    rclpy.init(args=args)
    node = aujvfcj()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()