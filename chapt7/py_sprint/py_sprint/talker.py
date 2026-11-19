import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class Talker(Node):
    def __init__(self):
        super().__init__('talker')                      # 节点名
        self.pub = self.create_publisher(Int32, 'count', 10)   # 话题名, 队列长度
        self.n = 0
        self.create_timer(1.0, self.tick)                # 1 秒一次 → 回调

    def tick(self):                                      # 回调函数
        msg = Int32()
        msg.data = self.n
        self.pub.publish(msg)
        self.get_logger().info(f'publish {self.n}')
        self.n += 1


def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)          # 单线程执行器，一直转，等回调
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
