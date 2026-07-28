# Note: this file is a template python-file and it was generated from config_file :E:/RobotVisionSuite/runtime/filtration.json.
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
    self.input = [[0,0,0,0,0]] # [[center_x,center_y,width,height,angle]
    self.output_indexs = []
    self.w = 0.000000
    self.h = 0.000000
    self.rote = 0.000000
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.input = input[0]
    self.w = float(input[1])
    self.h = float(input[2])
    self.rote = float(input[3])
    pass

  def outputData(self):
    return [ self.output_indexs ]

  def re_ini(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    pass
    

  def process(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    for i_idx,i in enumerate(self.input):
      if (i[2]<(self.w+self.w*self.rote) and i[2]>(self.w-self.w*self.rote)) and (i[3]<(self.h+self.h*self.rote) and i[3]>(self.h-self.h*self.rote)):
        self.output_indexs.append(str(i_idx))
    
  ############################################
  # ToDo: add your own function
  

##############################################
# ToDo: add your own code
