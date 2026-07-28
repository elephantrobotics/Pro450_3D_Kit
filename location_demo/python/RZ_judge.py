# Note: this file is a template python-file and it was generated from config_file :E:/RobotVisionSuite/runtime/RZ_judge.json.
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
    self.input = [0,0,0,0,0,0]
    self.output = [0.0,0.0,0.0,0.0,0.0,0.0]
    self.mode = "0"
    self.value = None
    self.positive = 0
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.input = input[0]
    self.positive = int(input[1])
    pass

  def outputData(self):
    return [ self.output, self.mode, self.value ]

  def re_ini(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    pass
    

  def process(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    self.positive=self.positive/180*3.141592
    if(self.positive>0):
      if (self.input[5]>0 and self.input[5]<self.positive):          
        self.mode="1"
        self.output=[0.0,0.0,0.0,0.0,0.0,3.141592]
      elif(self.input[5]< 0 and self.input[5]>(self.positive-3.141592)):
        self.mode="1"
        self.output=[0.0,0.0,0.0,0.0,0.0,-3.141592]     
      self.value=str(self.positive-180)
         
    else:      
      if(self.input[5]> 0 and self.input[5]>(self.positive+3.141592)) or (self.input[5]< 0 and self.input[5]<self.positive):
        self.mode="1"
        self.output=[0.0,0.0,0.0,0.0,0.0,3.141592]
      self.value=str(self.positive+180)
    
  ############################################
  # ToDo: add your own function
  

##############################################
# ToDo: add your own code
