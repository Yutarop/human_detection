#!/usr/bin/env python3
import math
import rclpy
import numpy as np
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs_py import point_cloud2  
from std_msgs.msg import Header


class PrePro(Node):
    def __init__(self):
        super().__init__("pre_processing")
        self.sub = self.create_subscription(
            PointCloud2, 'pcd_segment_obs', self.sr_call_back, 10
        )
        # puslish filtered pointcloud
        self.pub = self.create_publisher(PointCloud2, 'filtered_pointcloud2', 10)
    

    def sr_call_back(self, msg):
        point_cloud_data = point_cloud2.read_points(
            msg, field_names=("x", "y", "z", "intensity"), skip_nans=True
        )

        # Filter points by distance (0.5 m ~ 4 m にある点群のみを取り出す)
        filtered_points = self.filter_points_by_distance(point_cloud_data, min_distance=0.5, max_distance=4)

        # Create and publish the filtered PointCloud
        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = msg.header.frame_id
        fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
            PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1)
        ]
        filtered_pointcloud_msg = point_cloud2.create_cloud(header, fields, filtered_points)
        self.pub.publish(filtered_pointcloud_msg)

    def filter_points_by_distance(self, points, min_distance, max_distance):
        filtered_points = []

        for point in points:
            x, y, z, intensity = point
            distance = math.sqrt(x**2 + y**2)
            if min_distance <= distance:
                if distance <= max_distance:
                    # 人間の銅体あたりの点群を抽出できればいいと思ったので、高さの座標zが0.9 ~ 0.94 mにある点群のみを抽出. 適宜変えてください.
                    if 0.9 <= z <= 0.94:
                        z = 0 #z軸の情報はカットしました.
                        intensity = 0
                        filtered_points.append((x, y, z, intensity))

        return filtered_points


def main(args=None):
    rclpy.init(args=args)
    node = PrePro()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()