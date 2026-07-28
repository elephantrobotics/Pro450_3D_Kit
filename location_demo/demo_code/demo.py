# -*- coding: utf-8 -*-

import socket

import time
import numpy as np
from pymycobot import Pro450Client
import sys


class Visual_Grasping():
    def __init__(self):
        self.mc=Pro450Client()
        if self.mc.is_power_on()!=1:
            self.mc.power_on()
        self.mc.set_end_type(0)
        self.mc.set_base_io_output(1,0)
        conSuc_rvs, self.sock_rvs=self.connectRvsServer()
        self.robot_speed =20

        self.photo_point =[26.8, 25.04, -102.13, -15.94, -0.58, 72.2]
        self.a=[-25.56, -49.39, -50.63, 8.7, -2.69, 19.85]
        self.b=[64.03, -25.64, -89.26, 22.2, 1.29, 109.38]
        self.c=[-33.78, -23.95, -92.9, 25.93, -2.86, 11.62]
        self.d=[49.81, -53.42, -42.36, 2.84, 0.59, 95.18]

        self.target_name=["tee","elbow","ball_valve","through"]

        self.garb_changed=False
        self.old_pose=None
        # socket_buf_len = 1024
        # exec_index = 0

    def connectRvsServer(self,ip="localhost", port=2013):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            sock.connect((ip,port))
            print("ip:%s connected!" %(ip))
            return (True,sock)
        except Exception as e:
            sock.close()
            print("ip:%s disconnected!" %(ip))
            return (False,0)

    def disconnect (self,sock):
        if(sock):
            sock.close ()
            sock=None
        else:
            sock=None

    def get_send_TCP(self):
        result =self.mc.get_coords()
        robot_TCP = result.copy()
        print("***get tcp***%s"%time.asctime())
        print(result)
    
        resCutStr = ' '.join(repr(e) for e in result)    
        print(resCutStr) 
        #send tcp
        sendStr = "SET_POSE " + resCutStr + '#'
        print("***send tcp***%s"%time.asctime())
        print(sendStr) 
        self.sock_rvs.send(bytes(sendStr,encoding="utf-8"))
        print("***tcp_receive data***%s"%time.asctime())
        read_time=time.time()
        data=self.sock_rvs.recv(1024)
        print(data)
        print("read_time=",time.time()-read_time)

        data_arr = data.decode().split(",")
        print("data_arr =",data_arr[1] )
        if data_arr[1]=="false":
            print("Task completed")
            exit(0)
        pose_offet = [0, 0, 0, 0, 0, 0] 
        pose_real = [0, 0, 0, 0, 0, 0] 
        plane_grab_pose=[0, 0, 0, 0, 0, 0] 
        

        tmp1=data_arr[0].split()
        tmp2=data_arr[2].split()
        tmp3=data_arr[3].split()


        
        for j in range(0,6):
            pose_offet[j] = float(tmp1[j])
            pose_real[j] = float(tmp2[j])
            plane_grab_pose[j] = float(tmp3[j])


        # print("pose_offet=",pose_offet)
        # print("pose_real=",pose_real)
        # print("plane_grab_pose=",plane_grab_pose)
        # exit()

        return [pose_offet,pose_real,plane_grab_pose],data_arr[1]

    def six_degrees_of_freedom_grab(self,grab_pose):
   
        pose=grab_pose
        print("pose=",pose[:2])
          
        self.mc.send_coords(pose[0],self.robot_speed)       
        self.mc.send_coords(pose[1],self.robot_speed)

        self.mc.set_base_io_output(1,1)
        time.sleep(2)
                        
        self.mc.send_coords(pose[0],self.robot_speed)
        self.mc.send_angles(self.photo_point,self.robot_speed)

    def plane_grab(self,grab_pose):
        
        pose=grab_pose[2]
        print("pose=",pose)
        reference_pose=self.mc.get_coords() 
        for i in range(3,6):
            pose[i]=reference_pose[i]

            
        pose[2]+=160
        self.mc.send_coords(pose,self.robot_speed)
        pose[2]-=45
        self.mc.send_coords(pose,self.robot_speed)
        self.mc.set_base_io_output(1,1)
        time.sleep(2)                  
        pose[2]+=45
        self.mc.send_coords(pose,self.robot_speed)
        self.mc.send_angles(self.photo_point, self.robot_speed)
                        
                            

    def place(self,id):
        if id==self.target_name[0]:
            target=self.a
                           
        elif id==self.target_name[1]:
            target=self.b
                            
        elif id==self.target_name[2]:   
            target=self.c
                            
        elif id==self.target_name[3]:
            target=self.d


        self.mc.send_angles(target,self.robot_speed)
               
        self.mc.set_base_io_output(1,0)
        time.sleep(2)
    def photo(self):
        self.mc.send_angles(self.photo_point, self.robot_speed)
        time.sleep(1)

    def grab_policy(self,grab_pose):
        pose=grab_pose
        if self.old_pose is None:
            self.old_pose=pose[-1]
            robot.plane_grab(pose)
        else:      
            for i in range(2):
                diff=pose[-1][i]-self.old_pose[i]
                if abs(diff)<=3:
                    self.garb_changed=True                  
            if self.garb_changed:      
                robot.six_degrees_of_freedom_grab(pose)
                self.garb_changed=False
            else:       
                robot.plane_grab(pose)
            self.old_pose=pose[-1]


if __name__=="__main__":
    exec_index = 0
    robot=Visual_Grasping()
    while 1:
        try:
            exec_index = exec_index +1
            # print("第 %d 次拍照" %exec_index)
            robot.photo()
            pose,id=robot.get_send_TCP()
            robot.plane_grab(pose)
            robot.place(id)
            
        except KeyboardInterrupt:
            robot.mc.set_base_io_output(1,0)
            robot.mc.stop()
            robot.sock_rvs.close()
