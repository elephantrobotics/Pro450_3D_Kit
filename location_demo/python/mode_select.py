# Note: this file is a template python-file and it was generated from config_file :E:/RobotVisionSuite/runtime/mode_select.json.
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
    self.input_poselist = [[0,0,0,0,0,0]]
    self.mode = None
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.input_poselist = input[0]
    pass

  def outputData(self):
    return [ self.mode ]

  def re_ini(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    pass
    

  def process(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    if(len(self.input_poselist)==0):
      self.mode='1'
    else:
      self.mode='0'
    
  ############################################
  # ToDo: add your own function
  

##############################################
# ToDo: add your own code
