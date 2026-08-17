from pymycobot import Pro450Client
import time

er=Pro450Client()
if er.is_power_on()!=1:
    er.power_on()

er.set_end_type(0)
try:
    er.send_angles([0,0,0,0,0,0],10)
    er.send_angles([26.8, 25.04, -102.13, -15.94, -0.58, 72.2],10)
    er.set_base_io_output(1,1)
    time.sleep(2)
    er.set_base_io_output(1,0)
except:
    er.stop()
    er.set_base_io_output(1,0)
