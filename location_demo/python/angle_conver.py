# Note: this file is a template python-file and it was generated from config_file :D:/Program Files (x86)/RobotVisionSuite/runtime/angle_conver.json.
############################################
import RVS_LOG
# write log to RVS_log_file, for example:
# RVS_LOG.write('your own log string')
import numpy
from enum import Enum
import math
# ToDo: import the moudle you need


# The following class 'RVSPyClass' is the interface-class between your python_moudle and RVS.
class RVSPyClass:
  def __init__(self):
    # all io_port_name and para_name have been list as below.
    self.input = [[0,0,0,0,0,0]]
    self.out_put = []
    self.positive_min = 0
    self.positive_max = 0
    self.negative_min = 0
    self.negative_max = 0
    self.index = 0
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.input = input[0]
    self.positive_min = int(input[1])
    self.positive_max = int(input[2])
    self.negative_min = int(input[3])
    self.negative_max = int(input[4])
    self.index = int(input[5])
    pass

  def outputData(self):
    return [ self.out_put ]

  def re_ini(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    pass
    

  def process(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    RVS_LOG.write("RZ angle conversion ...")
    for i in self.input:
      if (self.negative_min == 0 and self.negative_max == 0):
        if (i[self.index] < self.positive_min and self.positive_min <= 180):
          i[self.index] = i[self.index] + 180
        if (i[self.index] > self.positive_max and self.positive_min >= 180):
          i[self.index] = i[self.index] - 180

      else:
        if (i[self.index] > 0):
          if (i[self.index] < self.positive_min or i[self.index] > self.positive_max):
            i[self.index] = i[self.index] - 180
        elif (i[self.index] < 0):
          if (i[self.index] < self.negative_min or i[self.index] > self.negative_max):
            i[self.index] = i[self.index] + 180

      self.out_put.append(i)
    
  ############################################
  # ToDo: add your own function
  

##############################################
# ToDo: add your own code
