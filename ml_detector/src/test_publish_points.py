#!/usr/bin/env python3

import rospy, sensor_msgs
from sensor_msgs.msg import PointCloud, ChannelFloat32
from geometry_msgs.msg import Point32

if __name__ == '__main__':
    rospy.init_node('point_cloud_publisher')
    cloud_pub = rospy.Publisher('cloud', sensor_msgs.msg.PointCloud, queue_size=150)

    num_points = 100

    count = 0
    r = rospy.Rate(1.0)
    while not rospy.is_shutdown():
        cloud = PointCloud()
        cloud.header.stamp = rospy.Time.now()
        cloud.header.frame_id = "jackal0/front_camera_optical"

        cloud.points = [Point32() for _ in range(num_points)]

        # we'll also add an intensity channel to the cloud
        cloud.channels = [ChannelFloat32()]
        cloud.channels[0].name = "intensities"
        cloud.channels[0].values = [None] * num_points

        # generate some fake data for our point cloud
        for i in range(num_points):
            cloud.points[i].x = 1 + count
            cloud.points[i].y = 2 + count
            cloud.points[i].z = 3 + count
            cloud.channels[0].values[i] = 100 + count

        cloud_pub.publish(cloud)
        count += 1
        # print(cloud.points, cloud.channels)
        r.sleep()

