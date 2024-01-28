#!/usr/bin/env python3.8

import rospy
import tf

from geometry_msgs.msg import TransformStamped
import tf2_ros
import geometry_msgs.msg
import tf_conversions

if __name__ == '__main__':
    rospy.init_node('robot_tf_publisher')
    broadcaster = tf2_ros.TransformBroadcaster()
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        t = geometry_msgs.msg.TransformStamped()
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = 'jackal0/base_link'
        t.child_frame_id = 'jackal0/front_camera_optical'
        # t.transform.translation.x = 0.007 + 0.12 #first summmand: same values as in the file accessories.urdf.xacro and maybe jackal.urdf (transformation to the top of the jackal)
        # t.transform.translation.y = 0.0 + 0.0 #second summand: values looked up in gazebo. Which file? (transformation to the 0 0 0 point of the base_link)
        # t.transform.translation.z = 0.02450 + 0.302
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)

        # new solution using rosrun tf2_tools echo.py jackal0/front_camera_optical jackal0/base_link to get the transform values
        t.transform.translation.x = 0.229
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.216
        t.transform.rotation.x = -0.5
        t.transform.rotation.y = 0.5
        t.transform.rotation.z = -0.5
        t.transform.rotation.w = 0.5
        broadcaster.sendTransform(t)
        rate.sleep()


# if __name__ == '__main__':
#     rospy.init_node('tf_broadcaster')
#     rospy.Subscriber('/%s/pose' % turtlename,
#                      turtlesim.msg.Pose,
#                      handle_turtle_pose,
#                      turtlename)
#     rospy.spin()

# #!/usr/bin/env python3
# import rospy

# # Because of transformations
# import tf_conversions

# import tf2_ros
# import geometry_msgs.msg
# import turtlesim.msg


# def handle_turtle_pose(msg, turtlename):
#     br = tf2_ros.TransformBroadcaster()
#     t = geometry_msgs.msg.TransformStamped()

#     t.header.stamp = rospy.Time.now()
#     t.header.frame_id = "world"
#     t.child_frame_id = turtlename
#     t.transform.translation.x = msg.x
#     t.transform.translation.y = msg.y
#     t.transform.translation.z = 0.0
#     q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
#     t.transform.rotation.x = q[0]
#     t.transform.rotation.y = q[1]
#     t.transform.rotation.z = q[2]
#     t.transform.rotation.w = q[3]

#     br.sendTransform(t)

# if __name__ == '__main__':
#     rospy.init_node('tf2_turtle_broadcaster')
#     turtlename = rospy.get_param('~turtle')
#     rospy.Subscriber('/%s/pose' % turtlename,
#                      turtlesim.msg.Pose,
#                      handle_turtle_pose,
#                      turtlename)
#     rospy.spin()