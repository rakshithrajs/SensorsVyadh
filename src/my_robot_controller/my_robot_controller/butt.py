import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Trigger
import json
import csv


class ButtonNode(Node):
    def __init__(self):
        super().__init__("button_node")
        self.subsa = self.create_subscription(String, "arduino_data", self.caller, 10)
        # global IR_sensor_data, US_sensor_data
        # IR_sensor_data = []
        # US_sensor_data = []
        global sensors
        sensors = {}
        self.sensor = self.create_service(Trigger, "get_avg_data", self.button_clicked)

    def average(self, list):
        return sum(list) / len(list)

    def caller(self, msg):
        # if (msg.data).split(":")[0] == "IR Reading":
        #     IR_data = (msg.data).split(":")[1]
        #     IR_sensor_data.append(float(IR_data))
        # else:
        #     US_data = (msg.data).split(":")[1]
        #     US_sensor_data.append(float(US_data))
        # if len(US_sensor_data) > 5:
        #     US_sensor_data.pop(0)
        # if len(IR_sensor_data) > 5:
        #     IR_sensor_data.pop(0)
        if (msg.data).split(":")[0] in list(sensors.keys()):
            if len(sensors[(msg.data).split(":")[0]]['data']) >= 5:
                sensors[(msg.data).split(":")[0]]['data'].pop(0)
            sensors[(msg.data).split(":")[0]]['data'].append(float((msg.data).split(":")[1]))
        else:
            sensors[(msg.data).split(":")[0]] = {'data': [], 'avg': 0}
        

    def button_clicked(self, response):
        for i in sensors:
            sensors[i]['avg'] = self.average(sensors[i]['data'])

        response.success = True
        with open("data.json", "w") as file:
            json.dump(sensors, file)
        with open("data.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(sensors.keys())
            writer.writerow(zip(sensors.values()))
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
