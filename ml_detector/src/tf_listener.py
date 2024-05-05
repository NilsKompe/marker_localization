#!/usr/bin/env python3
import rospy
import tf2_ros
from ml_msgs.msg import MarkerDetection
from geometry_msgs.msg import PointStamped, TransformStamped
import tf2_geometry_msgs.tf2_geometry_msgs


class Listener:
    def __init__(self):
        self.pub_base_point = rospy.Publisher("ml_landmarks/detected_markers_base_frame",MarkerDetection,queue_size=10)
        self.sub = rospy.Subscriber('ml_landmarks/detected_markers',MarkerDetection, self.callback_transform_point)
        self.tfBuffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tfBuffer)
    
    def callback_transform_point(self,msg):
    
        for marker in msg.markers:
            try:
                point_stamped = PointStamped()
                point_stamped.header = msg.header
                point_stamped.header.frame_id = "jackal0/front_camera_optical"
                point_stamped.point = marker.pose.position
                # self.tf_listener.waitForTransform("map", "jackal0/front_camera_optical", rospy.Time(0),rospy.Duration(4,0))
                # marker.pose.position = self.tf_listener.transformPoint("map", point_stamped).point
                transform = self.tfBuffer.lookup_transform("jackal0/base_link","jackal0/front_camera_optical",rospy.Time().now(),rospy.Duration(4,0))
                marker.pose.position = tf2_geometry_msgs.do_transform_point(point_stamped,transform).point
                # marker.pose.position = self.tf_listener.transformPoint("jackal0/base_link", point_stamped).point
                msg.header.frame_id = "jackal0/base_link"

                # rospy.loginfo("jackal0/front_camera_optical: (%.2f, %.2f. %.2f) -----> jackal0/base_link: (%.2f, %.2f, %.2f) at time %.2f",
                # point_stamped.point.x, point_stamped.point.y, point_stamped.point.z,
                # base_point.point.x, base_point.point.y, base_point.point.z, base_point.header.stamp.to_sec())

            except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as ex:
                rospy.logerr("Received an exception trying to transform a point from \"jackal0/front_camera_optical\" to \"jackal0/base_link\": %s", ex)

        self.pub_base_point.publish(msg)

if __name__ == '__main__':
    rospy.init_node('tf_listener')
    Listener()

    rospy.spin()

