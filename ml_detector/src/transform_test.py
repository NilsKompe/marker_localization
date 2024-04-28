#!/usr/bin/env python3
import numpy as np
import rospy
import tf2_ros
from ml_msgs.msg import MarkerDetection
from geometry_msgs.msg import PointStamped, TransformStamped
import tf2_geometry_msgs.tf2_geometry_msgs
from scipy.spatial.transform import Rotation



class Listener:
    def __init__(self):
        # self.start_time = time.time()
        self.tfBuffer = tf2_ros.Buffer()
        tf2_ros.TransformListener(self.tfBuffer)
        self.tfBuffer.can_transform_full
        rospy.sleep(1)
        self.last_transform_odom = self.tfBuffer.lookup_transform("map","jackal0/base_link",rospy.Time.now(),rospy.Duration(1,0))
        self.sub = rospy.Subscriber('ml_landmarks/detected_markers',MarkerDetection, self.callback_transform_point)
    
    def callback_transform_point(self,msg):
        # time_one = rospy.Time.now()
        
        time_now =rospy.Time.now()
        try:
            current_transform_odom = self.tfBuffer.lookup_transform("map","jackal0/base_link",rospy.Time.now(),rospy.Duration(1,0))
        except:
            raise
        odom = self.subtract_vector3(current_transform_odom.transform.translation,self.last_transform_odom.transform.translation)
        print("odom:", odom)
        distance_traveled = (odom[0]**2 + odom[1]**2)**0.5
        print("distance_traveled:", distance_traveled)
        euler_old = Rotation.from_quat([self.last_transform_odom.transform.rotation.x,self.last_transform_odom.transform.rotation.y,self.last_transform_odom.transform.rotation.z,self.last_transform_odom.transform.rotation.w]).as_euler("xyz",degrees=True)[2]
        euler_new = Rotation.from_quat([current_transform_odom.transform.rotation.x,current_transform_odom.transform.rotation.y,current_transform_odom.transform.rotation.z,current_transform_odom.transform.rotation.w]).as_euler("xyz",degrees=True)[2]
        changed_orientation = euler_new - euler_old
        print("changed_orientation:", changed_orientation)
        self.last_transform_odom = self.tfBuffer.lookup_transform("map","jackal0/base_link",rospy.Time.now(),rospy.Duration(1,0))
  
    def subtract_vector3(self,vec1,vec2):
        result_vector = [vec1.x-vec2.x,vec1.y-vec2.y,vec1.z-vec2.z]
        return result_vector

    def subtract_quaternion(self,quat1,quat2):
        result_quat = [quat1.x-quat2.x,quat1.y-quat2.y,quat1.z-quat2.z,quat1.w-quat2.w]
        for e in result_quat:
            if e != 0.0:
                return result_quat,True 
        return result_quat,False
if __name__ == '__main__':
    rospy.init_node('transform_test')
    Listener()

    rospy.spin()

