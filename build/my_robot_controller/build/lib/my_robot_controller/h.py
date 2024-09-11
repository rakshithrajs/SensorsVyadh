import serial
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class H(Node):
    def __init__(self):
        super().__init__("h")
        self.publisher_ = self.create_publisher(String, "arduino_data", 10)
        self.arduino = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1)
        time.sleep(2)
        self.get_logger().info("Serial port opened")
        self.timer = self.create_timer(0.1, self.read_from_arduino)

    def read_from_arduino(self):
        if self.arduino.in_waiting > 0:
            line = self.arduino.readline().decode("utf-8").rstrip()
            if line:
                self.get_logger().info(f"Received: {line}")
                msg = String()
                msg.data = line
                self.publisher_.publish(msg)

    def destroy_node(self):
        self.arduino.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = H()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
