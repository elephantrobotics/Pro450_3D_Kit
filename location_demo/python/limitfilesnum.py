# Note: this file is a template python-file and it was generated from config_file :D:/RobotVisionSuite/runtime/limitfilesnum.json.
############################################
import RVS_LOG
# write log to RVS_log_file, for example:
# RVS_LOG.write('your own log string')
import numpy
import os
import shutil
from enum import Enum
# ToDo: import the moudle you need


# The following class 'RVSPyClass' is the interface-class between your python_moudle and RVS.
class RVSPyClass:
  def __init__(self):
    # all io_port_name and para_name have been list as below.
    self.directory_name = ''
    self.limit_files_num = 20
    ##########################################
    # ToDo: remove 'pass' and add your code for initial
    pass
    

  def inputData(self,input):
    self.directory_name = input[0]
    self.limit_files_num = int(input[1])
    pass

  def outputData(self):
    return [ ]

  def re_ini(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    pass
    

  def process(self):
    ##########################################
    # ToDo: remove 'pass' and add your code
    self.delete_oldest_subfolders(self.directory_name, self.limit_files_num)
    
  ############################################
  # ToDo: add your own function
  def delete_oldest_subfolders(self,folder_path, max_subfolders):
    subfolders = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    if len(subfolders) > max_subfolders:
        subfolders.sort(key=lambda x: os.path.getmtime(x))
        subfolders_to_delete = subfolders[:len(subfolders) - max_subfolders]
        for subfolder in subfolders_to_delete:
            shutil.rmtree(subfolder)

##############################################
# ToDo: add your own code
