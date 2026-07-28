# Note: this file is a template python-file and it was generated from config_file :D:/RobotVisionSuite/runtime/heightp_judg.json.
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
    self.input_pose = [0,0,0,0,0,0]
    self.input_max = ''
    self.mode = None
    self.output_pose = None
    self.value = 0.060000
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.input_pose = input[0]
    self.input_max = input[1]
    self.value = float(input[2])
    pass

  def outputData(self):
    return [ self.mode, self.output_pose ]

  def re_ini(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    pass
    

  def process(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    f=abs(float(self.input_max)-float(self.input_pose[2]))
    print("f:"+str(f))
    self.output_pose=self.input_pose
    if f>self.value:
      self.mode='1'
      self.output_pose[2]=float(self.input_max)
    else:
      self.mode='0'
    
  ############################################
  # ToDo: add your own function
  

##############################################
# ToDo: add your own code
