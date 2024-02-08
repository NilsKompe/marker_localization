#!/usr/bin/env python3
import rospy
import tf2_ros
import tf
from ml_msgs.msg import MarkerDetection
# import ml_msgs/Marker
from geometry_msgs.msg import PointStamped
from sensor_msgs.msg import PointCloud, ChannelFloat32


def transformPoint(msg):
    # we'll create a point in the front_camera_optical frame that we'd like to transform to the base_link frame
    # front_camera_optical_msg = geometry_msgs.msg.PointStamped()
    # front_camera_optical_msg.header.frame_id = "jackal0/front_camera_optical"

    # # we'll just use the most recent transform available for our simple example
    # front_camera_optical_msg.header.stamp = rospy.Time()

    # # just an arbitrary point in space
    # front_camera_optical_msg.point.x = 1.0
    # front_camera_optical_msg.point.y = 0.2
    # front_camera_optical_msg.point.z = 0.0
    # print("6")
    # print(msg.markers[0].pose.position.x)
    # print("7")
    point_stamped = PointStamped()
    # print("8")
    point_stamped.header = msg.header
    point_stamped.header.frame_id = "jackal0/front_camera_optical"
    # print("9")
    pub_base_point = rospy.Publisher("detected_markers_base_frame",MarkerDetection)
    for marker in msg.markers:
        try:
            # print(marker.pose)
            point_stamped.point.x = marker.pose.position.x
            point_stamped.point.y = marker.pose.position.y
            point_stamped.point.z = marker.pose.position.z
            # print(point_stamped)
            base_point = listener.transformPoint("map", point_stamped)
            # base_point_marker_detection = MarkerDetection()
            # base_point_marker_detection.header = msg.header
            # base_point_marker_detection.markers = msg
            msg.header.frame_id = "map"
            marker.pose.position.x = base_point.point.x 
            marker.pose.position.y = base_point.point.y
            marker.pose.position.z = base_point.point.z

            pub_base_point.publish(msg)
            rospy.loginfo("jackal0/front_camera_optical: (%.2f, %.2f. %.2f) -----> map: (%.2f, %.2f, %.2f) at time %.2f",
                point_stamped.point.x, point_stamped.point.y, point_stamped.point.z,
                base_point.point.x, base_point.point.y, base_point.point.z, base_point.header.stamp.to_sec())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as ex:
            rospy.logerr("Received an exception trying to transform a point from \"jackal0/front_camera_optical\" to \"map\": %s", ex)

if __name__ == '__main__':
    print("1")
    rospy.init_node('tf_listener')
    # listener = tf.TransformListener(rospy.Duration(10))
    # we'll transform a point once every second
    #rospy.Timer(rospy.Duration(1.0), lambda event: transformPoint(listener))
    print("2")
    listener = tf.TransformListener(rospy.Duration(10))
    print("3")
    # sub = rospy.Subscriber('cloud',PointCloud, transformPoint)
    sub = rospy.Subscriber('ml_landmarks/detected_markers',MarkerDetection, transformPoint)
    print("4")
    rospy.spin()
    print("10")


# def transformPoint(msg):
#     # we'll create a point in the front_camera_optical frame that we'd like to transform to the base_link frame
#     # front_camera_optical_msg = geometry_msgs.msg.PointStamped()
#     # front_camera_optical_msg.header.frame_id = "jackal0/front_camera_optical"

#     # # we'll just use the most recent transform available for our simple example
#     # front_camera_optical_msg.header.stamp = rospy.Time()

#     # # just an arbitrary point in space
#     # front_camera_optical_msg.point.x = 1.0
#     # front_camera_optical_msg.point.y = 0.2
#     # front_camera_optical_msg.point.z = 0.0
#     print("6")
#     print(msg.points[0].x)
#     print("7")
#     point_stamped = PointStamped()
#     print("8")
#     point_stamped.header = msg.header
#     print("9")
#     for point in msg.points:
#         try:
#             point_stamped.point.x = point.x
#             point_stamped.point.y = point.y
#             point_stamped.point.z = point.z
#             base_point = listener.transformPoint("jackal0/base_link", point_stamped)
            
#             rospy.loginfo("jackal0/front_camera_optical: (%.2f, %.2f. %.2f) -----> jackal0/base_link: (%.2f, %.2f, %.2f) at time %.2f",
#                 point_stamped.point.x, point_stamped.point.y, point_stamped.point.z,
#                 base_point.point.x, base_point.point.y, base_point.point.z, base_point.header.stamp.to_sec())
#         except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as ex:
#             rospy.logerr("Received an exception trying to transform a point from \"jackal0/front_camera_optical\" to \"jackal0/base_link\": %s", ex)




# #include <ros/ros.h>
# #include <geometry_msgs/PointStamped.h>
# #include <tf/transform_listener.h>

# void transformPoint(const tf::TransformListener& listener){
#   //we'll create a point in the base_laser frame that we'd like to transform to the base_link frame
#   geometry_msgs::PointStamped laser_point;
#   laser_point.header.frame_id = "jackal0/front_camera_optical";

#   //we'll just use the most recent transform available for our simple example
#   laser_point.header.stamp = ros::Time();

#   //just an arbitrary point in space
#   laser_point.point.x = 1.0;
#   laser_point.point.y = 0.2;
#   laser_point.point.z = 0.0;

#   try{
#     geometry_msgs::PointStamped base_point;
#     listener.transformPoint("jackal0/base_link", laser_point, base_point);

#     ROS_INFO("jackal0/front_camera_optical: (%.2f, %.2f. %.2f) -----> jackal0/base_link: (%.2f, %.2f, %.2f) at time %.2f",
#         laser_point.point.x, laser_point.point.y, laser_point.point.z,
#         base_point.point.x, base_point.point.y, base_point.point.z, base_point.header.stamp.toSec());
#   }
#   catch(tf::TransformException& ex){
#     ROS_ERROR("Received an exception trying to transform a point from \"jackal0/front_camera_optical\" to \"jackal0/base_link\": %s", ex.what());
#   }
# }

# int main(int argc, char** argv){
#   ros::init(argc, argv, "robot_tf_listener");
#   ros::NodeHandle n;

#   tf::TransformListener listener(ros::Duration(10));

#   //we'll transform a point once every second
#   ros::Timer timer = n.createTimer(ros::Duration(1.0), boost::bind(&transformPoint, boost::ref(listener)));

#   ros::spin();

# }