# Note: this file is a template python-file and it was generated from config_file :D:/Program Files (x86)/RobotVisionSuite/runtime/Four_conver.json.
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
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.input = input[0]
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
    self.output=self.input
    for i_idx, i in enumerate(self.output):
      if i[3]>0 and i[3]<90:
        i[3]=0.0
        i[4]=0.0
      elif i[3]>0 and i[3]>=90:
        i[3]=180
        i[4]=180
      elif i[3]<0 and i[3]>=-90:
        i[3]=0.0
        i[4]=0.0
      else:
        i[3]=-180
        i[4]=-180       
    
  ############################################
  # ToDo: add your own function
  

##############################################
# ToDo: add your own code
