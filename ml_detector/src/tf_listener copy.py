#!/usr/bin/env python3
import rospy
import tf2_ros
import tf
import geometry_msgs.msg

def transformPoint(listener):
    # we'll create a point in the front_camera_optical frame that we'd like to transform to the base_link frame
    front_camera_optical_msg = geometry_msgs.msg.PointStamped()
    front_camera_optical_msg.header.frame_id = "jackal0/front_camera_optical"

    # we'll just use the most recent transform available for our simple example
    front_camera_optical_msg.header.stamp = rospy.Time()

    # just an arbitrary point in space
    front_camera_optical_msg.point.x = 1.0
    front_camera_optical_msg.point.y = 0.2
    front_camera_optical_msg.point.z = 0.0

    try:
        base_point = listener.transformPoint("jackal0/base_link", front_camera_optical_msg)
        rospy.loginfo("jackal0/front_camera_optical: (%.2f, %.2f. %.2f) -----> jackal0/base_link: (%.2f, %.2f, %.2f) at time %.2f",
            front_camera_optical_msg.point.x, front_camera_optical_msg.point.y, front_camera_optical_msg.point.z,
            base_point.point.x, base_point.point.y, base_point.point.z, base_point.header.stamp.to_sec())
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as ex:
        rospy.logerr("Received an exception trying to transform a point from \"jackal0/front_camera_optical\" to \"jackal0/base_link\": %s", ex)

if __name__ == '__main__':
    rospy.init_node('robot_tf_listener')
    listener = tf.TransformListener(rospy.Duration(10))
    # we'll transform a point once every second
    rospy.Timer(rospy.Duration(1.0), lambda event: transformPoint(listener))
    rospy.spin()



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