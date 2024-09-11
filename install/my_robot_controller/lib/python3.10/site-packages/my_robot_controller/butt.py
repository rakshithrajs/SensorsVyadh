import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Trigger
import json


class ButtonNode(Node):
    def __init__(self):
        super().__init__("button_node")
        self.subsa = self.create_subscription(String, "arduino_data", self.caller, 10)
        global IR_sensor_data, US_sensor_data
        IR_sensor_data = []
        US_sensor_data = []
        self.sensor = self.create_service(Trigger, "get_avg_data", self.button_clicked)

    def average(self, list):
        return sum(list) / len(list)

    def caller(self, msg):
        if (msg.data).split(":")[0] == "IR Reading":
            IR_data = (msg.data).split(":")[1]
            IR_sensor_data.append(float(IR_data))
        else:
            US_data = (msg.data).split(":")[1]
            US_sensor_data.append(float(US_data))
        if len(US_sensor_data) > 5:
            US_sensor_data.pop(0)
        if len(IR_sensor_data) > 5:
            IR_sensor_data.pop(0)

    def button_clicked(self, request, response):
        IR_avg = self.average(IR_sensor_data)
        US_avg = self.average(US_sensor_data)
        # avg = 0
        data = {"IR average": IR_avg, "US average": US_avg}
        response.success = True
        with open("data.json", "w") as file:
            json.dump(data, file)
        self.get_logger().info("Button clicked")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ButtonNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
