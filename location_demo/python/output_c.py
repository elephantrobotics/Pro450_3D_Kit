# Note: this file is a template python-file and it was generated from config_file :D:/Program Files (x86)/RobotVisionSuite/runtime/output_c.json.
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
    self.input = [[0,0,0,0,0,0]]
    self.output = []
    self.all_flag = False
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.input = input[0]
    self.all_flag = input[1] != 0
    pass

  def outputData(self):
    return [ self.output ]

  def re_ini(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    pass
    

  def process(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    self.output = []
    if self.all_flag:
      self.output=self.input 
    else:
      self.output.append(self.input[0])
    
  ############################################
  # ToDo: add your own function
  

##############################################
# ToDo: add your own code
