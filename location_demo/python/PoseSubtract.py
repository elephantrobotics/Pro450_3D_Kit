# Note: this file is a template python-file and it was generated from config_file :E:/RobotVisionSuite/runtime/PoseSubtract.json.
############################################
import RVS_LOG
# write log to RVS_log_file, for example:
# RVS_LOG.write('your own log string')
import numpy
from enum import Enum
# ToDo: import the moudle you need


# The following class 'RVSPyClass' is the interface-class between your python_moudle and RVS.
class RVSPyClass:
  def __init__(self):
    # all io_port_name and para_name have been list as below.
    self.input_pose1 = [0,0,0,0,0,0]
    self.input_pose2 = [0,0,0,0,0,0]
    self.angle_rx = ''
    self.output = None
    self.ouput_rx = None
    self.max_x = 0.000000
    self.min_x = 0.000000
    self.max_z = 0.000000
    self.min_z = 0.000000
    self.max_rx = 0.000000
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.input_pose1 = input[0]
    self.input_pose2 = input[1]
    self.angle_rx = input[2]
    self.max_x = float(input[3])
    self.min_x = float(input[4])
    self.max_z = float(input[5])
    self.min_z = float(input[6])
    self.max_rx = float(input[7])
    pass

  def outputData(self):
    return [ self.output, self.ouput_rx ]

  def re_ini(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    pass
    

  def process(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    self.max_x/=1000
    self.min_x/=1000
    self.max_z/=1000
    self.min_z/=1000
    self.max_rx=float(self.max_rx)/180*3.141592
    x=(self.input_pose2[0]-self.input_pose1[0])
    y=(self.input_pose2[1]-self.input_pose1[1])
    z=(self.input_pose2[2]-self.input_pose1[2])
    result="111"
    if x>self.max_x or x<self.min_x:
      result="011"
    elif z>self.max_z or z<self.min_z:
      result="101"
    elif float(self.angle_rx)>self.max_rx:
      result="110"
    x*=1000
    y*=1000
    z*=1000
    self.output=result+","+f"{x:.0f}"+","+f"{y:.0f}"+","+f"{z:.0f}"+";"
    self.ouput_rx=str(float(self.angle_rx)*180/3.141592)
    
  ############################################
  # ToDo: add your own function
  

##############################################
# ToDo: add your own code
