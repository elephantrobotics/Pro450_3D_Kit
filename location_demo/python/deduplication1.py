# Note: this file is a template python-file and it was generated from config_file :D:/Program Files (x86)/RobotVisionSuite/runtime/deduplication1.json.
############################################
import RVS_LOG
# write log to RVS_log_file, for example:
# RVS_LOG.write('your own log string')
import numpy
from enum import Enum
import copy
# ToDo: import the moudle you need


# The following class 'RVSPyClass' is the interface-class between your python_moudle and RVS.
class RVSPyClass:
  def __init__(self):
    # all io_port_name and para_name have been list as below.
    self.input_cube = [[0,0,0,0,0,0,1,1,1]]
    self.input_pose = [[0,0,0,0,0,0]]
    self.output_cube = []
    self.output_pose = []
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.input_cube = input[0]
    self.input_pose = input[1]
    pass

  def outputData(self):
    return [ self.output_cube, self.output_pose ]

  def re_ini(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    pass
    

  def process(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
      mid_cube_list = copy.deepcopy(self.input_cube)
      result_cube_list = copy.deepcopy(self.input_cube)
      result_pos_list = copy.deepcopy(self.input_pose)
      removed_idx_list = []
      for i_idx, i in enumerate(mid_cube_list):
        for j_idx, j in enumerate(mid_cube_list):
         if j_idx > i_idx:
           if j[0] <= i[0]+i[6]/2 and j[0] >= i[0]-i[6]/2 and j[1] <= i[1]+i[7]/2 and j[1] >= i[1]-i[7]/2:
             if j_idx not in removed_idx_list:
               result_cube_list.remove(j)
               result_pos_list.pop(j_idx)
               removed_idx_list.append(j_idx)

      self.output_cube = result_cube_list
      self.output_pose = result_pos_list
    
  ############################################
  # ToDo: add your own function
  

##############################################
# ToDo: add your own code
