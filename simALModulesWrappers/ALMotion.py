#!/usr/bin/env python

__author__ =        'Raphael LEBER'
__copyright__ = """

    Copyright 2019, CPE Lyon, Raphael LEBER

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License."""
    
__license__ =       'Apache 2.0'
__maintainer__ =    'Raphael LEBER'


import qi
#import pepper_kinematics as pk


class ALMotionProxy:
    
    def __init__(self, qiSession, sim_pepper):
        print("__init__ in ALMotionProxy")

        self.mem = qiSession.service("ALMemory")

        self.sim_pepper = sim_pepper  

        self._initNames()


   
    def _initNames(self):
        Head = ["HeadYaw", "HeadPitch" ]
        Leg = ["HipRoll", "HipPitch", "KneePitch"]
        LArm = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]
        RArm = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
        Torso = []
        Torso.extend(Head)
        Torso.extend(LArm)
        Torso.extend(RArm)
        Body = []
        Body.extend(Head)
        Body.extend(Leg)
        Body.extend(LArm)
        Body.extend(RArm)   
        self.BodyNames =    {
                                "Body" : Body,
                                "Torso": Torso,
                                "Head" : Head,
                                "Leg"  : Leg,
                                "LArm" : LArm,
                                "RArm" : RArm
                            }                                

    def move(self, x, y, theta):
        self.sim_pepper.move(x, y, theta)

    def moveTo(self, x, y, theta):
        self.sim_pepper.moveTo(x, y, theta)        

    def setAngles(self, joint_names, joint_values, percentage_speed):
        self.sim_pepper.setAngles(joint_names, joint_values, percentage_speed)   
        if isinstance(joint_names, list):
            for idx, joint_name in enumerate(joint_names):    
                name = "Device/SubDeviceList/"+joint_name+"/Position/Actuator/Value"
                self.mem.insertData(name, joint_values[idx])   
        else:
            name = "Device/SubDeviceList/"+joint_names+"/Position/Actuator/Value"
            self.mem.insertData(name, joint_values)    

    def getAngles(self, joint_names, useSensors):
        #print "getAngles ### " + joint_names
        if joint_names in self.BodyNames:
            joint_names = self.getBodyNames(joint_names)
        return self.sim_pepper.getAnglesPosition( joint_names )		

    def getRobotPosition(self, useSensors):
        return self.sim_pepper.getPosition( useSensors )	

    def getTransform(self, name, frame, useSensors):          
        #print "getTransform ### " + name 
        if name in self.BodyNames:
            name = self.getBodyNames(name)        
        return self.sim_pepper.getAnglesPosition( name )	  	

    def getPosition(self, name, frame, useSensorValues):
        
        if name in self.BodyNames:
            name = self.getBodyNames(name)
        #TODO: 
        # JUST TO RETURN THE RIGHT FORMAT BUT WRONG VALUES
        return [0, 0, 0, 0, 0, 0]    

    def getStiffnesses(self, joint_names):

        if joint_names in self.BodyNames:
            joint_names = self.getBodyNames(joint_names)
        stiffnesses = []
        for name in joint_names:
            #TODO : Put real values (if possible)
            stiffnesses.append(0.8)
        return stiffnesses

    def getBodyNames(self, name):
        return self.getJointNames(name)
    
    def getJointNames(self, name):	  
        if name in self.BodyNames: 
            return self.BodyNames[name]
        else:
            return []

    def robotIsWakeUp(self):
        return True

    def isRunning(self):
        return True    

